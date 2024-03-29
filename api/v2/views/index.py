#!/usr/bin/python3
""" Index test """
from models import storage
from api.v2.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def statusv2():
    """ Status of API """
    return jsonify({"status": "OK"})
