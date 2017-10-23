from flask_sqlalchemy import SQLAlchemy

#SQLAlchemy object - this will link to our flask app. it allows us to map objects (item/user)
#to rows in our database
db = SQLAlchemy()