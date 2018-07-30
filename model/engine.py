import settings.settings as settings

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Session:
    def __init__(self):
        self.__db_name = settings.config["db_name"]
        engine = create_engine("sqlite:///%s" % self.__db_name)
        self.__session = sessionmaker(bind=engine)()

    def __enter__(self):
        return self.__session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.commit()