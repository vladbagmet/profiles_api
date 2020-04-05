import attr


@attr.s
class Profile:
    platform = attr.ib()
    name = attr.ib()
    photo_url = attr.ib()
