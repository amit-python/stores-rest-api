#import sqlite3 - no need to import this now
from db import db

class ItemModel(db.Model): #tell sqlalchemy that ItemModel(class objects) are things that we will store/retrieve from database
#so that sqlalchemy creates mapping between database and the class objects. 
#models can come from database and sqlalchemy can pass into init method to create objects & models(objects) can be stored
# into database

#now tell sqlalchemy where these models are going to be stored
    __tablename__ = "items"    
#tell what columns table contains. So sqlalchemy now knows that model will have below three(now 4) columns
#and when it comes to saving to database, it will look for these three(now 4) only
    id = db.Column(db.Integer, primary_key=True) #primary key means it is unique and we are gonna create index from it
                                                #even though we dont have id on init function
    name = db.Column(db.String(80))    #80 chars max
    price = db.Column(db.Float(precision=2))
    
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))#Foreign key because it is linking to the 'id' field
                                                                #in a diff table called stores
    store = db.relationship('StoreModel')#'store' will contain object from StoreModel class to which the items belong
                                         #i.e. store_id in items table matches id in stores table
        
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
        
    def json(self):
        return {"name":self.name, "price":self.price}
    
    @classmethod
    def find_by_name(cls, name):
#        we will let sqlalchemy to the work here
#        sqlalchemy not only finds the row, it automatically converts it into object
        return cls.query.filter_by(name=name).first() # "query" is coming from db.Model class. we add a query using it
#        this is equal to SELECT * FROM __tablename__ WHERE name=name LIMIT 1
#        for further filtering we can do -> return ItemModel.query.filter_by(name=name).filter_by(id=1) and so on
#        or return ItemModel.query.filter_by(name=name, id=1)
    
#        connection = sqlite3.connect('data.db')
#        cursor = connection.cursor()
#        
#        query = "SELECT * FROM items WHERE name=?"
#        result = cursor.execute(query, (name,))
#        row = result.fetchone()
#        connection.close()
#        if row:
#            return cls(*row) #cls(row[0], row[1])
            
    def save_to_db(self): #previously "insert" method. This can do both insert and update
    
#        this insert (now save_to_db) method is saving the model to the database
#        sqlalchemy can directly translate object to row in a database
#        we just need to tell what object (model) to save into database. The object is self here
        db.session.add(self) #session here is a collection of objects that we are going to write to a database,
                            #we can write multiple objects, here we are only writing one(self)
        db.session.commit()
    
#        connection = sqlite3.connect('data.db')
#        cursor = connection.cursor()
#        
#        query = "INSERT INTO items VALUES (?, ?)"
#        cursor.execute(query, (self.name, self.price))
#        
#        connection.commit()
#        connection.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
#  ---------------      
#    def update(self): #no longer required as save_to_db method takes care
#        connection = sqlite3.connect('data.db')
#        cursor = connection.cursor()
#        
#        query = "UPDATE items SET price=? WHERE name=?"
#        cursor.execute(query, (self.price, self.name))
#        
#        connection.commit()
#        connection.close()