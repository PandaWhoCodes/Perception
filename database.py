# import sqlite3
#
# class database:
#     def __init__(self):
#
#         self.filename = "Perception.db"
#         self.table1 = "person"
#         self.table2 = "session"
#         self.table3 = "play"
#         self.table4 = "tags"
#
#         self.sql_do('create table if not exists ' + self.table1 + ' ( name TEXT,pid TEXT)')
#         self.sql_do('create table if not exists ' + self.table2 + ' ( pid TEXT,dateTime timestamp ,list_of_tags TEXT)')
#         self.sql_do('create table if not exists ' + self.table3 + ' ( key TEXT,no_of_people TEXT ,list_of_tags TEXT)')
#         self.sql_do('create table if not exists ' + self.table4 + ' ( key TEXT,no_of_people TEXT ,list_of_tags TEXT)')
#     def sql_do(self, sql, *params):
#         self._db.execute(sql, params)
#         self._db.commit()

from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///perception.db', echo=True)
Base = declarative_base()


########################################################################
class person(Base):
    """"""
    __tablename__ = "person"

    pid = Column(String, primary_key=True)
    name = Column(String)

    # items =Column(ARRA)
    # ----------------------------------------------------------------------
    def __init__(self, pid, name):
        """"""
        self.pid = pid
        self.name = name


class sessions(Base):
    """"""
    __tablename__ = "sessions"

    pid = Column(String)
    datetime = Column(DateTime)
    item = Column(String)  # items =Column(ARRA)
    sessid= Column(String,primary_key=True)

    # ----------------------------------------------------------------------
    def __init__(self, pid, datetime, item,sessid):
        """"""
        self.pid = pid
        self.datetime = datetime
        self.item = item  # create tables
        self.sessid=sessid
class play(Base):
    """"""
    __tablename__ = "play"

    pid = Column(String)
    item = Column(String)
    tag =Column(String)
    datetime = Column(DateTime)
    sessid= Column(String,primary_key=True)

    # playid= Column(String)

    # ----------------------------------------------------------------------
    def __init__(self, pid, item, tag,datetime,sessid):
        """"""
        self.pid = pid
        self.tag = tag
        self.item = item  # create tables
        self.datetime = datetime
        self.sessid = sessid


Base.metadata.create_all(engine)
