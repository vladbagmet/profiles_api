from flask import Blueprint, jsonify

from handlers.response_messages import MessageType
from app.classes.platforms import Platforms
from app.classes.storage import Storage

bp = Blueprint("users", __name__)


@bp.route("/", methods=["GET"])
def get_profiles():
    twitter_storage = Storage(Platforms.twitter)
    stored_profiles = twitter_storage.get_all_profiles()
    profiles = [{"name": p.name, "platform": p.platform, "photo_url": p.photo_url} for p in stored_profiles]
    return jsonify({"message": MessageType.data_retrieved.value, "profiles": profiles})
