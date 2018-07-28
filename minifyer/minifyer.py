from model.sqlite_model import UrlDAO


class Minifyer:
    def __init__(self, encoder):
        self.__encoder = encoder

    def minify(self, url: str) -> str:
        url = UrlDAO.create_url(url)
        encoded_enpoint = self.__encoder.encode(str(url.id))

        return encoded_enpoint

    def deminify(self, url: str) -> int:
        source_url_id = self.__encoder.decode(url)
        url = UrlDAO.get_url_by_id(source_url_id)

        return url.url