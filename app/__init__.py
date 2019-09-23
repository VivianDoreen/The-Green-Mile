from flask import Flask
from flask_cors import CORS
from database import DatabaseConnection
database_connection = DatabaseConnection()
database_connection.create_tables()

app = Flask(__name__)
CORS(app)
from app.views import users

