from bs4 import BeautifulSoup

from app.classes.abstract.parser import AbstractParser


class TwitterParser(AbstractParser):
    def get_picture_url(self, html: str) -> [str, None]:
        soup = BeautifulSoup(html, "lxml")
        react_container = soup.find(id='react-root')
        if react_container:
            image_tags = react_container.findAll('img')
            if image_tags:
                profile_images_tags = [
                    image_tag for image_tag in image_tags if "profile_images" in image_tag.attrs["src"]
                ]

                for profile_images_tag in profile_images_tags:
                    if "_bigger" not in profile_images_tag["src"]:
                        return profile_images_tag["src"]
