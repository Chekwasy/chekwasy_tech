#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.farm import Farm
from models.buildex import Buildex
from models.solar import Solar
from models.annie import Annie
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request



@app_views.route('/chekwasy_farm/2626632/all_order', methods=['GET'], strict_slashes=False)
def list_farm_user():
    """
    list all farm user
    """

    lst = []
    all_fm = storage.all(Farm).values()

    for dic in all_fm:
    	lst.append(dic.to_dict())
    return jsonify(lst)


@app_views.route('/chekwasy_farm/2626632/all_enquiry', methods=['GET'], strict_slashes=False)
def list_buildex_user():
    """
    list all farm user
    """

    lst = []
    all_fm = storage.all(Buildex).values()

    for dic in all_fm:
        lst.append(dic.to_dict())
    return jsonify(lst)

@app_views.route('/chekwasy_solar/2626632/all_order', methods=['GET'], strict_slashes=False)
def list_farm_user():
    """
    list all solar user
    """

    lst = []
    all_fm = storage.all(Solar).values()

    for dic in all_fm:
        lst.append(dic.to_dict())
    return jsonify(lst)

@app_views.route('/annie_couture/2626632/all_order', methods=['GET'], strict_slashes=False)
def list_annie_user():
    """
    list all farm user
    """

    lst = []
    all_fm = storage.all(Annie).values()

    for dic in all_fm:
        lst.append(dic.to_dict())
    return jsonify(lst)


@app_views.route('/chekwasy_farm/order', methods=['POST'], strict_slashes=False)
def post_farm_user():
    """
    Creates a farm user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")

    data = request.get_json()
    instance = Farm(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/chekwasy_buildex/enquiry', methods=['POST'], strict_slashes=False)
def post_buildex_user():
    """
    Creates a buildex user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")

    data = request.get_json()
    instance = Buildex(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/chekwasy_solar/order', methods=['POST'], strict_slashes=False)
def post_solar_user():
    """
    Creates a Solar user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")

    data = request.get_json()
    instance = Solar(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/annie_couture/order', methods=['POST'], strict_slashes=False)
def post_annie_user():
    """
    Creates a Annie user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")

    data = request.get_json()
    instance = Annie(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)
