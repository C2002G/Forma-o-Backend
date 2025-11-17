import sqlalchemy as sa

import databases

DATABASE_URL = "sqlite:///./blog.db"

database = databases.database(DATABASE_URL)
metadata = sa.MetaData()
engine = sa.create_engine(DATABASE_URL, connect_args={"chech_same_thread": False})
metadata.create_all(engine)
