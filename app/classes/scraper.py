import os

from app.classes.platforms import Platforms
from libs.utils import validate_platform


class Scraper:
    def __init__(self, platform: Platforms):
        validate_platform(platform)
        self._platform_url = platform.value
        self._platform_name = platform.name

    def process_profile(self, profile_name: str):
        # Running asynchronous parsing job in the background.
        os.system(
            f"python {os.getcwd()}/libs/background_parser.py "
            f"{self._platform_url}{profile_name} {profile_name} {self._platform_name} >> /dev/null &"
        )
