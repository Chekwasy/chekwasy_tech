#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.farm import Farm
from models.buildex import Buildex
from models.solar import Solar
from models.annie import Annie
from os import environ
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/', strict_slashes=False)
def chekwasy():
    """ Chekwasy is alive! """

    return render_template('chekwasy_tech.html')

@app.route('/chekwasy_farm', strict_slashes=False)
def chekwasy_farm():
    """ Chekwasy_farm is alive! """

    return render_template('chekwasy_farm.html')

@app.route('/chekwasy_buildex', strict_slashes=False)
def chekwasy_buildex():
    """ Chekwasy_buildex is alive! """

    return render_template('chekwasy_buildex.html')

@app.route('/chekwasy_solar', strict_slashes=False)
def chekwasy_solar():
    """ Chekwasy_solar is alive! """

    return render_template('chekwasy_solar.html')

@app.route('/annie_couture', strict_slashes=False)
def chekwasy_annie():
    """ Annie Couture is alive! """

    return render_template('chekwasy_annie.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
