from flask import Flask
from app.views.index import app

if __name__ == '__main__':
    app.run(port=5000, debug='true')
