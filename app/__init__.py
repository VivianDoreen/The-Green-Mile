from flask import Flask
from database import DatabaseConnection
database_connection = DatabaseConnection()
database_connection.create_tables()

app = Flask(__name__)
