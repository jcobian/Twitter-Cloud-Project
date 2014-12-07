#!/usr/bin/python
# -*- mode: python -*-
#
# Core app code that launches the actual application

from flask import Flask, render_template
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

# Current time ranges
# 2014-02-19 00:00:00 to 2014-02-25 23:59:59
# 2014-02-26 00:00:00 to 2014-03-04 23:59:59
# 2014-03-05 00:00:00 to 2014-03-11 23:59:59
# 2014-03-12 00:00:00 to 2014-03-18 23:59:59
# 2014-03-19 00:00:00 to 2014-03-25 23:59:59
# 2014-03-26 00:00:00 to 2014-04-01 23:59:59
# 2014-04-02 00:00:00 to 2014-04-09 23:59:59
@app.route("/")
@app.route("/timeRange/<int:timeRangeIndex>")
def getDataInTimeRange(timeRangeIndex=1):
    timeRangeIndex = int(timeRangeIndex)
    if timeRangeIndex == 1:
        pass
    elif timeRangeIndex == 2:
        pass
    elif timeRangeIndex == 3:
        pass
    elif timeRangeIndex == 4:
        pass
    elif timeRangeIndex == 5:
        pass
    elif timeRangeIndex == 6:
        pass
    elif timeRangeIndex == 7:
        pass
    else:
        # Return some kind of error message
        pass
    return render_template('timeRange.html', rangeIndex=timeRangeIndex)
	

if __name__ == '__main__':
    # Set to false before deployment
    # Allows server to update on code changes without having to restart it
    app.debug = True
    app.run(host='0.0.0.0')
