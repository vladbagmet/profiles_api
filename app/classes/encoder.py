import base64


class Encoder:
    def __init__(self):
        self.encoding = "utf-8"

    def encode(self, to_encode: str) -> str:
        url_safe_encoded_bytes = base64.urlsafe_b64encode(to_encode.encode(self.encoding))
        return str(url_safe_encoded_bytes, self.encoding)

    def decode(self, to_decode: str) -> str:
        return str(base64.b64decode(to_decode), self.encoding)
