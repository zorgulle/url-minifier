from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///toto.sql")
session = sessionmaker(bind=engine)()