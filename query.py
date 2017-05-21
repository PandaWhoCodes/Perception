import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
from Perception.database import *

engine = create_engine('sqlite:///perception.db', echo=True)

# create a Session
Session = scoped_session(sessionmaker(bind=engine))
session = Session()

# Create objects
# for student in session.query(Student).order_by(Student.id):
#     print(student.firstname, student.lastname)
import random
def getItem():
    with open('word.txt','r') as f:
        a=f.read().split('\n')
        return random.choice(a)

# def get