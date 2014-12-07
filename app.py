#!/usr/bin/python
# -*- mode: python -*-
#
# Core app code that launches the actual application

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

#------------------------------------------------------------------------
# Database connection and setup

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://masteruser:_cloud2014@cloudprojectdb.cqwak4ataijt.us-east-1.rds.amazonaws.com:3306/cloudproject'
db = SQLAlchemy(app)

class Tweet(db.Model):
    __tablename__ = 'Tweet'
    __table_args__ = {'autoload':True, 'autoload_with':db.engine}

#TODO: Add other tables here

#------------------------------------------------------------------------
# URL Routing

@app.route("/")
def test():
    output = ''; 
    for item in db.session.query(Tweet).filter(Tweet.Favorites > 20):
        output += str(item.TweetID) + '<br>'

    return output

if __name__ == '__main__':
    # Set to false before deployment
    # Allows server to update on code changes without having to restart it
    app.debug = True
    app.run(host='0.0.0.0')
