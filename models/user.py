#import sqlite3
from db import db


#UserModel is kind of like an API (not a REST API though), is an interface for other parts of program to interact with database
class UserModel(db.Model): #tell sqlalchemy that UserModel (class objects) are things that we will store/retrieve from database
#so that sqlalchemy creates mapping between database and the class objects
#models can come from database and sqlalchemy can pass into init method to create objects and objects can be stored into database

#now tell sqlalchemy where these models are going to be stored
    __tablename__ = "users"
#tell what columns table contains. So sqlalchemy now knows that model will have below three columns
#and when it comes to saving to database, it will look for these three only
#    id is built-in but should still be fine here
    id = db.Column(db.Integer, primary_key=True) #primary key means it is unique and we are gonna create index from it
    username = db.Column(db.String(80))    #80 chars max
    password = db.Column(db.String(80))
    
    def __init__(self, username, password):
        self.username=username
        self.password=password
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first() # check ItemModels (item.py) for more details
            
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first() # check ItemModels (item.py) for more details