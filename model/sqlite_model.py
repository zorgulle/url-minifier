from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
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