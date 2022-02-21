import os
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


db_path = os.path.join(os.getcwd(), 'testDB.sqlite3')
engine = create_engine(f'sqlite:///{db_path}')
metadata = MetaData(bind=engine)
Base = declarative_base()


class Region(Base):
    __table__ = Table('regions', metadata, autoload=True)

    def get_region_cities(self):
        with Session(engine) as session:
            query = session.query(City).filter(self.id == City.region_id)
            return query.all()


class City(Base):
    __table__ = Table('cities', metadata, autoload=True)


class User(Base):
    __table__ = Table('users', metadata, autoload=True)


def get_total():
    with Session(engine) as session:
        query = session.query(User, City, Region)\
            .join(City, User.city == City.id)\
            .join(Region, User.region == Region.id)
        return query.all()


def get_regions():
    with Session(engine) as session:
        query = session.query(Region).order_by('region_name')
        return query.all()
