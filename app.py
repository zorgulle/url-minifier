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


class Encoder:
    @staticmethod
    def encode(to_encode):
        return base64.standard_b64encode(to_encode.encode("utf-8")).decode("utf-8")

    @staticmethod
    def decode(to_decode):
        return base64.standard_b64decode(to_decode.encode("utf-8")).decode("utf-8")


class Minifyer:
    @staticmethod
    def minify(url: str) -> str:
        url = UrlDAO.create_url(url)
        x = Encoder.encode(str(url.id))

        return x

    @staticmethod
    def deminify(url: str) -> int:
        x = Encoder.decode(url)
        url = UrlDAO.get_url_by_id(x)

        return url.url

if __name__ == "__main__":
    x = Minifyer.minify("www.google2.com")
    print(x)
    x = Minifyer.deminify(x)
    print(x)