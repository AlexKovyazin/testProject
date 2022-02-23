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

    def create_user(self):
        with Session(engine) as session:
            session.add(self)
            session.commit()


def get_total():
    with Session(engine) as session:
        query = session.query(User, City, Region)\
            .join(City, User.city == City.id, isouter=True)\
            .join(Region, User.region == Region.id, isouter=True)
        return query.all()


def replace_none(query):
    for join in query:
        for obj in join:
            if obj is None:
                continue
            for column in obj.__table__.columns:
                value = getattr(obj, column.name)
                if value is None:
                    setattr(obj, column.name, '')
    return query


def get_regions():
    with Session(engine) as session:
        query = session.query(Region).order_by('region_name')
        return query.all()


def get_region_cities(region_id):
    with Session(engine) as session:
        query = session.query(City).filter(City.region_id == region_id)
        return query.all()


def as_dict(obj):
    """
    Возвращает объект sqlalchemy в виде словаря
    :param obj: объект БД <__main__.(название класса) object at ...
    :return: dict
    """
    return {column.name: getattr(obj, column.name) for column in obj.__table__.columns}


def query_as_dict(query):
    """
    Аналогично as_dict() но применимо к query
    :param query: список объектов БД
    :return: dict
    """
    result = []
    for obj in query:
        result.append(as_dict(obj))
    return result
