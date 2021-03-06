#import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', #anything other than username will be rejected in request
                            type=str,
                            required=True,
                            help = "This field cannot be left blank!")  
        
    parser.add_argument('password', #anything other than password will be rejected in request
                            type=str,
                            required=True,
                            help = "This field cannot be left blank!")  
                            
    def post(self):
        data = UserRegister.parser.parse_args()
           
                            
        if UserModel.find_by_username(data['username']):
            return {"message":"User already exists"}, 400
        
        user = UserModel(**data) #UserModel(data['username'], data['password'])
        user.save_to_db()
                    
#        connection = sqlite3.connect('data.db')
#        cursor = connection.cursor()
#        
#        query="INSERT INTO users VALUES (NULL, ?, ?)"
#        cursor.execute(query, (data['username'], data['password']))
#        
#        connection.commit()
#        connection.close()
        return {"message":"User created successfully!"}, 201
        
