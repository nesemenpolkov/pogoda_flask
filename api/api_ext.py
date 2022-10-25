from flask import make_response, jsonify


def make_api_response(success, response, status):
    return make_response(jsonify({ "success": success, "response": response }), status)


def success(response="", status=200):
    return make_api_response(True, response, status)


def error(response="", status=400):
    return make_api_response(False, response, status)