from flask import Flask, render_template, request, redirect, jsonify, flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, TimeCount
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
def getDataSec():
    engine = create_engine('sqlite:///dEarly.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    timecounts = session.query(TimeCount).order_by(desc(TimeCount.timestamp)).limit(1)
    return jsonify(timecounts=[r.serialize for r in timecounts])

@app.route('/datasecall')
def getDataSecAll():
    engine = create_engine('sqlite:///dEarly.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    timecounts = session.query(TimeCount).order_by(desc(TimeCount.timestamp)).limit(60)
    return jsonify(timecounts=[r.serialize for r in timecounts])

# Custom error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.secret_key = "ajsdlfkajfdsjiofad"
    app.debug = True
    app.run(host='0.0.0.0', port=5000)