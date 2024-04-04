from flask import Blueprint, jsonify, request

from src.errors.error_handler import handle_error
from src.data.event_handler import EventHandler
from src.http_types.http_request import HttpRequest

event_route_bp = Blueprint("event_route", __name__)


@event_route_bp.route("/events", methods=["POST"])
def create_event():
    try:
        http_request = HttpRequest(body=request.json)
        event_handler = EventHandler()
        response = event_handler.register(http_request)

        return jsonify(response.body), response.status_code
    except Exception as exception:
        response = handle_error(exception)

        return jsonify(response.body), response.status_code


@event_route_bp.route("/events/<event_id>", methods=["GET"])
def get_event(event_id):
    try:
        event_handler = EventHandler()
        http_request = HttpRequest(param={"event_id": event_id})
        response = event_handler.find_by_id(http_request)

        return jsonify(response.body), response.status_code
    except Exception as exception:
        response = handle_error(exception)

        return jsonify(response.body), response.status_code
