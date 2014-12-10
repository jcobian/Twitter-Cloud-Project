#!/usr/bin/python
# -*- mode: python -*-
#
# Core app code that launches the actual application

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import json
from bs4 import BeautifulSoup
import urllib2

app = Flask(__name__)

#------------------------------------------------------------------------
# Database connection and setup

instanceAddress = 'http://ec2-54-164-93-32.compute-1.amazonaws.com:5000'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://masteruser:_cloud2014@cloudprojectdb.cqwak4ataijt.us-east-1.rds.amazonaws.com:3306/cloudproject'
db = SQLAlchemy(app)

class Tweet(db.Model):
    __tablename__ = 'Tweet'
    __table_args__ = {'autoload':True, 'autoload_with':db.engine}

class TopHashtag(db.Model):
    __tablename__ = 'TopHashtag'
    __table_args__ = {'autoload':True, 'autoload_with':db.engine}

class TopLink(db.Model):
    __tablename__ = 'TopLink'
    __table_args__ = {'autoload':True, 'autoload_with':db.engine}

class TopImage(db.Model):
    __tablename__ = 'TopImage'
    __table_args__ = {'autoload':True, 'autoload_with':db.engine}

class TopKeyword(db.Model):
    __tablename__ = 'TopKeyword'
    __table_args__ = {'autoload':True, 'autoload_with':db.engine}

class TopLinkTest(db.Model):
    __tablename__ = 'TopLinkTest'
    __table_args__ = {'autoload':True, 'autoload_with':db.engine}


db.session.commit()

#-----------------------------------------------------------------------
# Queries to database

tweetLocations = list()

def getInfoForDateRange(startTime, endTime):
	keywords = list()
	for keyword in db.session.query(TopKeyword).filter(TopKeyword.StartRange == startTime, TopKeyword.EndRange == endTime):
		keywords.append(keyword.Keyword)
	hashtags = list()
	for hashtag in db.session.query(TopHashtag).filter(TopHashtag.StartRange == startTime, TopHashtag.EndRange == endTime):
		hashtags.append(hashtag.Hashtag)
	images = list()
	for image in db.session.query(TopImage).filter(TopImage.StartRange == startTime, TopImage.EndRange == endTime):
		images.append(image.Image)
	links = list()
	for link in db.session.query(TopLinkTest).filter(TopLinkTest.StartRange == startTime, TopLinkTest.EndRange == endTime):
		d = dict()
		d['url'] = link.Link
		d['title'] = link.Title
		links.append(d)
	del tweetLocations[:]
	for location in db.session.query(Tweet).filter(Tweet.Lat != None, Tweet.Lng != None, Tweet.Time > startTime, Tweet.Time < endTime):
		tweetLocations.append({'lat': str(location.Lat), 'lng': str(location.Lng)})
	return keywords, hashtags, images, links

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
	kw, ht, img, lk = getInfoForDateRange('2014-02-19 00:00:00', '2014-02-25 23:59:59')
	tr = '2/19 - 2/25'
    elif timeRangeIndex == 2: 
	kw, ht, img, lk = getInfoForDateRange('2014-02-26 00:00:00', '2014-03-04 23:59:59')
	tr = '2/26 - 3/4'
    elif timeRangeIndex == 3:
	kw, ht, img, lk = getInfoForDateRange('2014-03-05 00:00:00', '2014-03-11 23:59:59')
	tr = '3/5 - 3/11'
    elif timeRangeIndex == 4:
	kw, ht, img, lk = getInfoForDateRange('2014-03-12 00:00:00', '2014-03-18 23:59:59')
	tr = '3/12 - 3/18'
    elif timeRangeIndex == 5:
	kw, ht, img, lk = getInfoForDateRange('2014-03-19 00:00:00', '2014-03-25 23:59:59')
	tr = '3/19 - 3/25'
    elif timeRangeIndex == 6:
	kw, ht, img, lk = getInfoForDateRange('2014-03-26 00:00:00', '2014-04-01 23:59:59')
	tr = '3/26 - 4/1'
    elif timeRangeIndex == 7:
	kw, ht, img, lk = getInfoForDateRange('2014-04-02 00:00:00', '2014-04-09 23:59:59')
	tr = '4/2 - 4/9'
    else:
    	kw = ['Error: No data in that time range']
    	lk = kw
	img = kw
	ht = kw
	tr = ''
    return render_template('timeRange.html', instance=instanceAddress, timeRange=tr, topKeywords=kw, topHashtags=ht, topImages=img, topLinks=lk)

@app.route("/tweetLocations")
def getTweetLocations():
	return json.dumps(tweetLocations, separators=(',', ': '))	

if __name__ == '__main__':
    app.run(host='0.0.0.0')
