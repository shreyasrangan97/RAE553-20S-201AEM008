import sqlite3
from flask_restful import Resource, reqparse

class UserRegister(Resource):
    parser = reqparse.RequestParser()

    #Including price to the argument.
    parser.add_argument('username', type=str,required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str,required=True, help='This field cannot be left blank')

    #creating users by defining post
    def post(self):
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data['username']):
            return {"message":"A user with this username is already exists"}, 400
        connection = sqlite3.connect('data.db')
        cursor =   connection.cursor()
        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'],data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully"}, 201

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    #verifying the username and checking the existance
    @classmethod
    def find_by_username(cls, username):
        connection  = sqlite3.connect('data.db')
        cursor =   connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        #data which matches the parameter is selected from the slected row in the database.
        result = cursor.execute(query, (username,))

        #for obtaining single value.
        row = result.fetchone()
        #first row is selected
        if row:
        #matching an id, username and password of the user.
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
    #checking the database for id.
    @classmethod
    def find_by_id(cls, id):
        connection  = sqlite3.connect('data.db')
        cursor =   connection.cursor()

        query = "SELECT * FROM users WHERE id=?" #choosing the id that is similar from all the available rows in the database.
        result = cursor.execute(query, (id,)) #for obtaing single value.
        row = result.fetchone() #from the result opting the first row.
        if row:
            #selecting the row those match an id,

            user = cls(*row)
        else:
            user = None # if there is no object available.

        connection.close()
        return user
