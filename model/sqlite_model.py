from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from model.engine import Session

Base = declarative_base()


class Urls(Base):
    __tablename__ = "Urls"
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String)

class UrlDAO:
    @staticmethod
    def create_url(url):
        with Session() as session:
            url = Urls(url=url)
            session.add(url)
            session.flush()
        return url

    @staticmethod
    def get_url_by_id(url_id):
        with Session() as session:
            return session.query(Urls).filter_by(id=int(url_id)).first()