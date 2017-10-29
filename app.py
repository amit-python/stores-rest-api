from flask import Flask
from flask_restful import Api
from security import authenticate, identity
from flask_jwt import JWT
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app=Flask(__name__)

#specify database name and path and database type. can use any other sql database as well like postgresql, oracle, etc
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.db'

#a configuration property. related to tracking an object is changed but not saved to database
#this turns off flask-sqlalchemy modifiction tracker but it does not turn of the sqlalchemy mod tracker which is better
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key='jose'
api=Api(app)


jwt=JWT(app, authenticate, identity) #create /auth end point


#below are resources created (endpoints).
#This is something through which client requests from a server or server responds to client 
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

#To avoid running the app on import we do below so the app will run only if it is run as main function, i.e. directly (no import)
if __name__ == '__main__':
    from db import db # impoting here bcs of circular imports, Item resource imports Itemmodel which too imports db
    db.init_app(app) # pass our flask app to SQLAlechmy object
    app.run(port=5000, debug=True)