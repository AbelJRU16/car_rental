from flask import Response
import json

def make_response(data, code):
    response = Response(json.dumps(data), status=code, mimetype='application/json')
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return response