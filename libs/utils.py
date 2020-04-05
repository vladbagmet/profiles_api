from app.classes.platforms import Platforms


def validate_platform(platform: Platforms):
    if platform not in [p for p in Platforms]:
        raise ValueError(f"`{platform}` is unexpected platform")
