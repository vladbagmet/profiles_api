from typing import List, Tuple
import os

from app.classes.abstract.storage import AbstractStorage
from app.classes.platforms import Platforms
from libs.utils import validate_platform
from app.classes.encoder import Encoder
from app.classes.profile import Profile
from config import config


class Storage(AbstractStorage):
    def __init__(self, platform: Platforms):
        self._storage_path = f"{os.getcwd()}/{config.STORAGE_FOLDER_NAME}"
        self._init_storage(platform)
        self._platform = platform
        self._storage_platform_path = f"{self._storage_path}/{platform.name}"
        self._encoder = Encoder()  # We need encoder because urls are not valid file names for the file system.
        self._delimiter = "|"

    def set_profile(self, name: str, url: str) -> None:
        file_name = f"{self._storage_platform_path}/{name}{self._delimiter}{self._encoder.encode(url)}"
        with open(file_name, "w") as file:
            file.write("")

    def get_profile(self, name: str) -> [Profile, None]:
        files = [f for f in os.listdir(self._storage_platform_path) if f and f.startswith(f"{name}{self._delimiter}")]
        if files:
            return Profile(self._platform.name, *self._get_profile_data(files[0]))

    def get_all_profiles(self) -> List[Profile]:
        return [
            Profile(self._platform.name, *self._get_profile_data(f)) for f in os.listdir(self._storage_platform_path)
        ]

    def _get_profile_data(self, storage_file_name: str) -> Tuple[str, str]:
        if self._delimiter not in storage_file_name:
            raise ValueError(f"storage file `{storage_file_name}` has incorrect file name format, please delete it")
        split_list = storage_file_name.split(self._delimiter)
        return split_list[0], self._encoder.decode(split_list[1])

    def _init_storage(self, platform):
        validate_platform(platform)
        storage_platform_path = f"{self._storage_path}/{platform.name}"
        if not os.path.exists(storage_platform_path):
            os.makedirs(storage_platform_path)
