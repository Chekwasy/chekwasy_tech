#!/usr/bin/python3
""" Starts a Flash Web Application """
import requests
from models import storage
from models.farm import Farm
from models.buildex import Buildex
from models.solar import Solar
from models.annie import Annie
from models.farm_order import Farm_order
from os import environ
from flask import Flask, render_template, request, abort, redirect
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

lst = ['farm_session_id']

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.before_request
def filteringrequest():
    """function to filter out routes that dont need authentication"""
    farm_lock_paths = [
        '/farm_user/',
        '/farm_user',
        '/farm_profile/',
        '/farm_profile',
        '/farm_order/',
        '/farm_order',
        '/farm_update/',
        '/farm_update',
    ]

    if (request.path in farm_lock_paths):
        from api.v2.app import AUTH
        cooki = request.cookies.get("farm_session_id")
        if (cooki is None):
            redirect('/farm_login')
        if cooki:
            resp = requests.get("http://chekwasy.tech/api/v2/farm_check/" + cooki)
            if resp.status_code != 200:
                redirect('/farm_login')


@app.route('/', strict_slashes=False)
def chekwasy():
    """ Chekwasy is alive! """

    return render_template('chekwasy_tech.html')

@app.route('/farm', strict_slashes=False)
def chekwasy_farm():
    """ Chekwasy_farm is alive! """

    return render_template('chekwasy_farm.html')

@app.route('/buildex', strict_slashes=False)
def chekwasy_buildex():
    """ Chekwasy_buildex is alive! """

    return render_template('chekwasy_buildex.html')

@app.route('/solar', strict_slashes=False)
def chekwasy_solar():
    """ Chekwasy_solar is alive! """

    return render_template('chekwasy_solar.html')

@app.route('/nansannie', strict_slashes=False)
def chekwasy_annie():
    """ Annie Couture is alive! """

    return render_template('chekwasy_annie.html')

@app.route('/farm_login', strict_slashes=False)
def farm_login():
    """ login for farm """

    return render_template('farm_login.html')

@app.route('/farm_fpwd', strict_slashes=False)
def farm_fpwd():
    """ forgot pwd for farm """

    return render_template('farm_forgot_pwd.html')

@app.route('/farm_register', strict_slashes=False)
def farm_reg():
    """Register user for farm """

    return render_template('farm_register.html')

@app.route('/farm_tk', strict_slashes=False)
def farm_pass_reset():
    """ Token reset pwd for farm """

    return render_template('farm_reset_pwd.html')

@app.route('/farm_user', strict_slashes=False)
def farm_user():
    """ signed in for user for farm """

    return render_template('farm_signedin.html')

@app.route('/farm_order', strict_slashes=False)
def farm_order():
    """ order form for farm """

    return render_template('farm_order.html')

@app.route('/farm_profile', strict_slashes=False)
def farm_profile():
    """ profile for user for farm """

    return render_template('farm_profile.html')

@app.route('/farm_update', strict_slashes=False)
def farm_update():
    """ update profile for user for farm """

    return render_template('farm_update.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
