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

class Minifyer:

    @staticmethod
    def minify(url: str) -> str:
        import base64

        url = Urls(url=url)
        session.add(url)
        session.flush()

        x = base64.standard_b64encode(str(url.id).encode("utf-8"))

        session.commit()

        return x.decode("utf-8")

    @staticmethod
    def deminify(url: str) -> int:
        import base64

        x = base64.standard_b64decode(url.encode("utf-8"))
        url = session.query(Urls).filter_by(id=int(x)).first()

        return url.url

if __name__ == "__main__":
    x = Minifyer.minify("www.google2.com")
    print(x)
    x = Minifyer.deminify(x)
    print(x)