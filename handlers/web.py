from http import HTTPStatus

from flask import Flask, jsonify
from flask_cors import CORS
import trafaret as t

from handlers.response_messages import MessageType
from handlers.api import scrape, user, users


app = Flask(__name__)
app.register_blueprint(scrape.bp, url_prefix='/scrape')
app.register_blueprint(user.bp, url_prefix='/user')
app.register_blueprint(users.bp, url_prefix='/users')
CORS(app)


@app.route('/', methods=['GET'])
def index_route():
    return jsonify({'message': MessageType.service_health.value})


@app.errorhandler(t.DataError)
def handle_validation_violations(error):
    return jsonify(
        {'message': MessageType.validation_error.value, 'error': error.as_dict()}
    ), HTTPStatus.UNPROCESSABLE_ENTITY


@app.errorhandler(400)
def handle_bad_requests(error):
    return jsonify(
        {'message': MessageType.request_error.value, 'error': 'unable to parse json payload'}
    ), HTTPStatus.BAD_REQUEST


@app.errorhandler(404)
def handle_not_found_page_requests(error):
    return jsonify({'message': MessageType.not_found.value, 'error': f'{error}'.lower()}), HTTPStatus.NOT_FOUND


@app.errorhandler(405)
def handle_not_found_method_requests(error):
    return jsonify(
        {'message': MessageType.not_allowed.value, 'error': f'{error}'.lower()}
    ), HTTPStatus.METHOD_NOT_ALLOWED


@app.errorhandler(500)
def handle_server_errors(error):
    return jsonify(
        {'message': MessageType.server_error.value, 'error': 'failed to process the request'}
    ), HTTPStatus.INTERNAL_SERVER_ERROR
