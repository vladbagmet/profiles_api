from http import HTTPStatus

from flask import Blueprint, request, jsonify

from handlers.response_messages import MessageType
from handlers.validators import TWITTER_HANDLE
from app.classes.platforms import Platforms
from app.classes.scraper import Scraper

bp = Blueprint("scrape", __name__)


@bp.route("/", methods=["POST"])
def scrape_handle():
    json_data = request.get_json()
    TWITTER_HANDLE.check(json_data)
    profile_name = json_data["handle"]
    twitter_scraper = Scraper(Platforms.twitter)
    twitter_scraper.process_profile(profile_name)
    return jsonify({"message": MessageType.handle_processed.value}), HTTPStatus.ACCEPTED
