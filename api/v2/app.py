#!/usr/bin/python3
""" Flask Application """
from flask_mail import Mail
from models import storage
from api.v2.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify, abort, request,redirect
from flask_cors import CORS
from api.v2.auth.auth import Auth
AUTH = Auth()
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'chekwasybuildex@gmail.com'
app.config['MAIL_PASSWORD'] = 'ucblaybosshvkvwt'
mail = Mail(app)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v2/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.before_request
def filteringrequest():
    """function to filter out routes that dont need authentication
    users: where post done to create user
    sessions: where post done to comfim valid login and log user in by generating new session
    reset_password: where post is done to generate token and also put to reset pwd
    verify: verify user email
    """
    if AUTH is None:
        return
    excluded_paths = [
        '/api/v2/unauthorized/',
        '/api/v2/forbidden/',
        '/api/v2/farm_reset_password/',
        '/api/v2/farm_users/',
        '/api/v2/farm_sessions/',
        '/api/v2/farm_verify/',
        '/api/v2/farm_check/*',
    ]
    if not AUTH.require_auth(request.path, excluded_paths):
        return

    cooki = request.cookies.get("farm_session_id")
    if (cooki is None):
        abort(401)
    if cooki:
        usr = AUTH.get_farm_user_from_session_id(cooki)
        if usr is None:
            abort(403)


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ 401 Error
    ---
    responses:
      401:
        description: unautorized access
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def unauthorized(error) -> str:
    """ 403 Error
    ---
    responses:
      403:
        description: forbidden access
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)



if __name__ == "__main__":
    """ Main Function """
    host = environ.get('CHEKWASY_API_HOST')
    port = environ.get('CHEKWASY_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5001'
    app.run(host=host, port=port, threaded=True)
