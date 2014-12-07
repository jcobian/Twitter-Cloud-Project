#!/usr/bin/python
# -*- mode: python -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://masteruser:_cloud2014@cloudprojectdb.cqwak4ataijt.us-east-1.rds.amazonaws.com:3306/cloudproject'
db = SQLAlchemy(app)

class Tweet(db.Model):
    __tablename__ = 'Tweet'
    __table_args__ = {'autoload':True, 'autoload_with':db.engine}

@app.route("/")
def hello():
    output = ''; 
    for item in db.session.query(Tweet).filter(Tweet.Favorites > 20):
        output += str(item.TweetID) + '\n'

    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
