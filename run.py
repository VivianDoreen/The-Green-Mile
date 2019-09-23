from flask import Flask
from app.views.index import app
from app.views.users import app
import os

if __name__ == '__main__':
    app.run(port=5000, debug='true')
