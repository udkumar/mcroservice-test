from flask import Flask, make_response, json, g, request, jsonify, redirect
from flask_restful import Resource, Api, reqparse
import config
import datetime
import time
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')


api = Api(app)
ma = Marshmallow(app)

cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

import ikea_app.routes.routes

if app.config['DEBUG']:
    app.debug = True


def conf_logging(app):
    """
    Setup proper logging
    """

    if app.debug is True:
        from ikea_app.ikea_file_handler import IkeaFileHandler
        import logging
        file_handler = IkeaFileHandler(app.config['LOG_FILE'],
                                                   maxBytes=1024 * 1024 * 100,
                                                   backupCount=31)
        if app.config['LOG_LEVEL'] == 'INFO':
            file_handler.setLevel(logging.INFO)
        elif app.config['LOG_LEVEL'] == 'DEBUG':
            file_handler.setLevel(logging.DEBUG)
        elif app.config['LOG_LEVEL'] == 'WARNING':
            file_handler.setLevel(logging.WARNING)
        else:
            file_handler.setLevel(logging.ERROR)
        formatter = logging.Formatter("%(asctime)s - %(name)s - "
                                      "%(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(file_handler.level)


conf_logging(app)



@app.before_request
def start_timer():
    g.start = time.time()


@app.after_request
def log_request(response):
    if request.path == '/favicon.ico':
        return response
    elif request.path.startswith('/static'):
        return response

    now = time.time()
    duration = round(now - g.start, 2)
    dt = datetime.datetime.fromtimestamp(now)

    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    host = request.host.split(':', 1)[0]
    args = dict(request.args)
    log_params = [
        ('method', request.method),
        ('path', request.path),
        ('status', response.status_code),
        ('duration', duration),
        ('ip', ip),
        ('host', host),
    ]

    request_id = request.headers.get('X-Request-ID')
    if request_id:
        log_params.append(('request_id', request_id, 'yellow'))

    app.logger.info(log_params)

    return response


@api.representation('application/json')
def output_json(data, code, headers=None):
    if code == 400 or code == 401:
        data['status'] = 0
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp