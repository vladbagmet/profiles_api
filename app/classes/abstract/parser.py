from abc import ABC, abstractmethod


class AbstractParser(ABC):
    @abstractmethod
    def get_picture_url(self, html: str) -> str:
        raise NotImplementedError
