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

# Current time ranges
# 2014-02-19 18:13:00 to 2014-02-25 23:36:59
# 2014-02-26 00:17:00 to 2014-03-04 23:59:59
# 2014-03-05 00:00:00 to 2014-03-11 23:59:59
# 2014-03-12 00:00:00 to 2014-03-18 23:59:59
# 2014-03-19 00:00:00 to 2014-03-25 23:59:59
# 2014-03-26 00:00:00 to 2014-04-01 23:59:59
# 2014-04-02 00:00:00 to 2014-04-08 23:59:59
# 2014-04-09 00:00:00 to 2014-04-09 03:31:59
@app.route("/time_range/<int:time_range_index>")
def getDataInTimeRange(timeRangeIndex):
    if timeRange == 1:
        pass
    elif timeRange == 2:
        pass
    elif timeRange == 3:
        pass
    elif timeRange == 4:
        pass
    elif timeRange == 5:
        pass
    elif timeRange == 6:
        pass
    elif timeRange == 7:
        pass
    else:
        # Return some kind of error message
        pass
	

if __name__ == '__main__':
    # Set to false before deployment
    # Allows server to update on code changes without having to restart it
    app.debug = True
    app.run(host='0.0.0.0')
