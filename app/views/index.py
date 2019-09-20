from flask import Flask
from app import app


@app.route('/')
def index():
    """
    Index route
    :return:
    """
    return "<h2>Welcome to Green Mile</h2> The most efficient company in the whole world. Try us, you will see"
