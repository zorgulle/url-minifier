engine = create_engine("sqlite:///toto.sql")
session = sessionmaker(bind=engine)()