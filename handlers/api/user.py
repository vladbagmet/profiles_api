from http import HTTPStatus

from flask import Blueprint, jsonify

from handlers.response_messages import MessageType
from handlers.validators import TWITTER_HANDLE
from app.classes.platforms import Platforms
from app.classes.storage import Storage

bp = Blueprint("user", __name__)


@bp.route("/<handle>/profile_pic", methods=["GET"])
def get_profile(handle):
    TWITTER_HANDLE.check({"handle": handle})
    twitter_storage = Storage(Platforms.twitter)
    profile = twitter_storage.get_profile(handle)
    if profile:
        return jsonify(
            {
                "message": MessageType.data_retrieved.value,
                "profile": {"name": profile.name, "platform": profile.platform, "photo_url": profile.photo_url}
            }
        )
    else:
        return jsonify({"message": MessageType.profile_not_found.value}), HTTPStatus.NOT_FOUND
