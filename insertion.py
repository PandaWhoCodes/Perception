import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from Perception.database import *

engine = create_engine('sqlite:///perception.db', echo=True)

# create a Session
Session = scoped_session(sessionmaker(bind=engine))
session = Session()


def getpItem(pid):
    a=[]
    for student in session.query(sessions).filter(sessions.pid == pid):
        a.append(student.item)
    return a[(len(a)-1)]

def getTags(item):
    a=[]
    for student in session.query(play).filter(play.item == item):
        a.append(student.tag)
    return a

def setTags(pid, item, tag, sessid):
    insertPlay(pid, item, tag, sessid)


def rollback1():
    session.rollback()


def setSession(pid, item, sessid):
    insertSession(pid, item, sessid)


def setPerson(pid, name, ):
    insertPerson(pid, name)


def setPlay(pid, item, a, sessid):
    insertPlay(pid, item, a, sessid)


def insertPerson(pid, name, ):
    user = person(pid, name)
    session.add(user)
    session.commit()


def insertSession(pid, item, sessid):
    sess = sessions(pid, datetime.datetime.now(), item, sessid)
    session.add(sess)
    session.commit()


def insertPlay(pid, item, tag, sessid):
    rep = play(pid, item, tag, datetime.datetime.now(), sessid)
    session.add(rep)
    session.commit()
