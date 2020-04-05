from abc import ABC, abstractmethod
from typing import List

from app.classes.profile import Profile


class AbstractStorage(ABC):
    @abstractmethod
    def set_profile(self, name: str, url: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_profile(self, name: str) -> [Profile, None]:
        raise NotImplementedError

    @abstractmethod
    def get_all_profiles(self) -> List[Profile]:
        raise NotImplementedError
