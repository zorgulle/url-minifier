import base64

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///toto.sql")
session = sessionmaker(bind=engine)()

Base = declarative_base()

class Urls(Base):
    __tablename__ = "Urls"
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String)

class UrlDAO:
    @staticmethod
    def create_url(url):
        url = Urls(url=url)
        session.add(url)
        session.flush()
        session.commit()
        return url

    @staticmethod
    def get_url_by_id(url_id):
        return session.query(Urls).filter_by(id=int(url_id)).first()


class StringEncoding:
    @staticmethod
    def encode(to_encode):
        return to_encode.encode("utf-8")
    @staticmethod
    def decode(to_decode):
        return to_decode.decode("utf-8")

class Encoder:
    @staticmethod
    def encode(to_encode):
        raise NotImplementedError
    @staticmethod
    def decode(to_decode):
        raise NotImplementedError


class Base64EncoderStrategy(Encoder):
    @staticmethod
    def encode(to_encode):
        encoded_string = StringEncoding.encode(to_encode)
        base_64_encoded_id = base64.standard_b64encode(encoded_string)
        decoded_string = StringEncoding.decode(base_64_encoded_id)

        return decoded_string

    @staticmethod
    def decode(to_decode):
        encoded_string = StringEncoding.encode(to_decode)
        base_64_decoded_id = base64.standard_b64decode(encoded_string)
        decoded_string = StringEncoding.decode(base_64_decoded_id)

        return decoded_string


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

if __name__ == "__main__":
    minifyier = Minifyer(Base64EncoderStrategy())

    x = minifyier.minify("www.google2.com")
    print(x)
    x = minifyier.deminify(x)
    print(x)