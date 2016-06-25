from flask import Flask, render_template, request, redirect, jsonify, flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
# from database_setup import Base, User, Developer, Game
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import random
import requests

app = Flask(__name__)

# engine = create_engine('sqlite:///gamecatalog.db')
# Base.metadata.bind = engine

# DBSession = sessionmaker(bind=engine)
# session = DBSession()

# HTML pages
# Show index (latest games and all developers)
@app.route('/')
@app.route('/index/')
def showIndex():
    return render_template('index.html')

@app.route('/datasec')
def getDataSec(): # TODO
    return str(random.randrange(0, 10))

@app.route('/datasecall')
def getDataSecAll(): # TODO
    return str(random.randrange(0, 10))

# Custom error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.secret_key = "ajsdlfkajfdsjiofad"
    app.debug = True
    app.run(host='0.0.0.0', port=5000)