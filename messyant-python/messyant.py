import os
import pypyodbc
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

def sql_conn():
    conn = pypyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server="+ os.environ['DATABASE_ENDPOINT'] + ";"
                          "Database=" + os.environ['DATABASE_NAME'] + ";"
                          "uid=" + os.environ['DATABASE_ENDPOINT_USERNAME'] +
                          ";pwd=" + os.environ['DATABASE_ENDPOINT_PASSWORD'] + ";")
    return conn.cursor()

class User (Resource):
   def get(self):
      cursor = sql_conn()
      cursor.execute('SELECT * FROM User')
      return { "response" : cursor }

api.add_resource(User, '/') # Route_1

if __name__ == '__main__':
   app.run('0.0.0.0','8080')
