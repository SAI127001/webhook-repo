from flask import Blueprint, request, jsonify
from .models import save_event
from .utils import format_event

bp = Blueprint('routes', __name__)

@bp.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    event_type = request.headers.get('X-GitHub-Event')
    
    if not data:
        return jsonify({"error": "No data received"}), 400

    parsed = format_event(data, event_type)
    if parsed:
        save_event(parsed)
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "ignored event"}), 204

@bp.route('/events', methods=['GET'])
def get_events():
    from .models import get_all_events
    return jsonify(get_all_events())

