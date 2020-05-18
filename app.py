from flask import Flask, request #Importing Flask from Flask module
from flask_restful import Resource, Api, abort, reqparse #extracting resource, api, abort, reqparse from flask restful to get rest Api
from flask_jwt import JWT, jwt_required, current_identity # import JWT, jwt_required, current_identity from flask_jwt

from security import authenticate, identity #importing authenticate, identity from security
from user import UserRegister
from item import Item

app = Flask(__name__) # creating Flask application
app.secret_key = 'shreyas' #Including secret key.
api = Api(app) # creating api application instance using this command

jwt = JWT(app, authenticate, identity) #creating an object for JWT and endpoint is also added for flask_jwt register


api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')
if __name__ == '__main__':
    app.run(debug=True)
#RAE553_201AEM008
