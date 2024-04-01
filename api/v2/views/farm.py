#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Farm user """
from models.farm import Farm
from models.farm_order import Farm_order
from models import storage
from api.v2.views import app_views
from flask_mail import Message
from flask import abort, jsonify, make_response, request, redirect
import random
"""from flasgger.utils import swag_from"""


@app_views.route('/farm_users', methods=[
    'POST'], strict_slashes=False)
def reg_farm_userv2() -> str:
    """register a farm user to the server"""
    data = request.get_json()
    if not data:
        abort(404)
    email = data.get("email")
    password = data.get("password")
    if email and password:
        try:
            from api.v2.app import AUTH
            usr = AUTH.register_farm_user(email, password)
            return jsonify({"email": usr.email,
                            "message": "user created"})
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


@app_views.route('/farm_sessions', methods=[
    'POST'], strict_slashes=False)
def farm_loginv2() -> str:
    """method to comfirm farm logged in"""
    data = request.get_json()
    if not data:
        abort(404)
    email = data.get("email")
    password = data.get("password")
    from api.v2.app import AUTH
    if AUTH.valid_farm_login(email, password):
        uid = AUTH.create_farm_session(email)
        response = jsonify({"email": email, "message": "logged in", "sess": uid})
        response.set_cookie("farm_session_id", uid, max_age=900)
        return response
    else:
        abort(401)


@app_views.route('/farm_sessions', methods=[
    'DELETE'], strict_slashes=False)
def farm_logoutv2():
    """method to delete farm session. same as logout"""
    cooki = request.cookies.get("farm_session_id")
    if cooki is None:
        abort(404)
    from api.v2.app import AUTH
    usr = AUTH.get_farm_user_from_session_id(cooki)
    if usr is None:
        return jsonify([])
    AUTH.destroy_farm_session(usr.id)
    return jsonify([])


@app_views.route('/farm_check/<sess>', methods=[
    'GET'], strict_slashes=False)
def check(sess) -> str:
    """method to check user by session_id"""
    if sess is None:
        abort(403)
    from api.v2.app import AUTH
    usr = AUTH.get_farm_user_from_session_id(sess)
    if usr is None:
        abort(404)
    return jsonify({"email": usr.email}), 200


@app_views.route('/farm_reset_password', methods=[
    'POST'], strict_slashes=False)
def get_farm_reset_password_token() -> str:
    """method to get a reset password token"""
    from api.v2.app import mail
    data = request.get_json()
    if not data:
        abort(404)
    email = data.get("email")
    try:
        from api.v2.app import AUTH
        r_tok = AUTH.get_farm_reset_password_token(email)
        if r_tok is None:
            abort(403)
        msg = Message('Chekwasy Farm Reset Password Token', sender='chekwasybuildex@gmail.com', recipients=[email])
        msg.body = f"Copy and paste your reset password token below \n {r_tok}"
        mail.send(msg)
        return jsonify({"email": email, "reset_token": r_tok})
    except ValueError:
        abort(403)


@app_views.route('/farm_reset_password', methods=[
    'PUT'], strict_slashes=False)
def farm_update_password() -> str:
    """route to update password for farm user"""
    data = request.get_json()
    if not data:
        abort(404)
    email = data.get("email")
    reset_token = data.get("reset_token")
    new_password = data.get("new_password")
    try:
        from api.v2.app import AUTH
        AUTH.update_farm_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"})
    except ValueError:
        abort(403)

@app_views.route('/farm_profile', methods=[
    'GET'], strict_slashes=False)
def farm_profile() -> str:
    """route to get details for farm user"""
    cooki = request.cookies.get("farm_session_id")
    if cooki is None:
        abort(403)
    from api.v2.app import AUTH
    usr = AUTH.get_farm_user_from_session_id(cooki)
    if usr is None:
        abort(403)
    info = usr.to_dict()
    return jsonify({"first_name": info.get("first_name"), "last_name": info.get("last_name"), "email": info.get("email"), "phone": info.get("phone"), "address": info.get("street") + " " + info.get("city") + " " + info.get("state")}), 201


@app_views.route('/farm_order', methods=[
    'GET'], strict_slashes=False)
def get_farm_order() -> str:
    """route to get orders for farm user"""
    cooki = request.cookies.get("farm_session_id")
    if cooki is None:
        abort(403)
    from api.v2.app import AUTH
    usr = AUTH.get_farm_user_from_session_id(cooki)
    if usr is None:
        abort(403)
    all_order = storage.all(Farm_order).values()
    usr_order = []
    for some in all_order:
        if some.user_id == usr.id:
            usr_order.append[some]
    order_dt = []
    if len(usr_order) > 0:
        for sm in usr_order:
            order_dt.append(sm.to_dict())
        for a in order_dt:
            del a["user_id"]

    return jsonify(order_dt)


@app_views.route('/farm_order', methods=[
    'POST'], strict_slashes=False)
def farm_order() -> str:
    """route to post order for farm user"""
    cooki = request.cookies.get("farm_session_id")
    if cooki is None:
        abort(403)
    from api.v2.app import AUTH
    usr = AUTH.get_farm_user_from_session_id(cooki)
    if usr is None:
        abort(403)
    data = request.get_json()
    if not data:
        abort(404)
    order_qty = data.get("order_qty")
    note = data.get("note")
    from api.v2.app import mail

    log = {"user_id": usr.id, "order_qty": order_qty, "note": note}

    order = Farm_order(**log)
    order.save()
    msg = Message('Chekwasy Farm. Order Information', sender='chekwasybuildex@gmail.com', recipients=[usr.email])
    msg.body = f"Thank You For Your Order.\n Your Order ID Is {order.id} \n For Reference Purpose"
    mail.send(msg)
    return jsonify("Success"), 201


@app_views.route('/farm_profile', methods=[
    'PUT'], strict_slashes=False)
def farm_update_profile() -> str:
    """route to put update for farm user profile"""
    cooki = request.cookies.get("farm_session_id")
    if cooki is None:
        abort(403)
    usr_dt = request.get_json()
    if not usr_dt:
        abort(404)
    from api.v2.app import AUTH
    first_name = usr_dt.get("first_name")
    last_name = usr_dt.get("last_name")
    phone = usr_dt.get("phone")
    street = usr_dt.get("street")
    city = usr_dt.get("city")
    state = usr_dt.get("state")
    dt = {"first_name": first_name, "last_name": last_name, "phone": phone, "street": street, "city": city, "state": state}
    try:
        AUTH.update_farm_usr(cooki, dt)
        return jsonify("Success"), 201
    except ValueError:
        return


@app_views.route('/farm_verify', methods=[
    'GET'], strict_slashes=False)
def farm_verify() -> str:
    """method to check user valid email for farm"""
    usr_dt = request.get_json()
    if not usr_dt:
        abort(404)
    from api.v2.app import mail
    email = usr_dt.get("email")
    num = random.randint(103737, 998789)
    msg = Message('Chekwasy Farm. Email Verify Token', sender='chekwasybuildex@gmail.com', recipients=[email])
    msg.body = f"Enter The Token Below To Comfirm Your Email Address\n {num}"
    mail.send(msg)
    return jsonify({"verify_token": str(num)}), 200
