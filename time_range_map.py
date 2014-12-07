#!/usr/bin/python
import sys
import ast
import datetime

def getMonthNum(month):
	if month == "Jan":
		return "01"
	if month == "Feb":
		return "02"
	if month == "Mar":
		return "03"
	if month == "Apr":
		return "04"
	if month == "May":
		return "05"
	if month =="Jun":
		return "06"
	if month == "Jul":
		return "07"
	if month =="Aug":
		return "08"
	if month =="Sep":
		return "09"
	if month =="Oct":
		return "10"
	if month =="Nov":
		return "11"
	if month =="Dec":
		return "12"

def getTime(created_at):
	tokens = created_at.split()
	year = tokens[5]
	month = getMonthNum(tokens[1])
	day = tokens[2]
	clocktime = tokens[3].split(":")
	hour = clocktime[0]
	minutes = clocktime[1]
	#secs = clocktime[2]
	#tweet_time = "%s-%s-%s %s:%s" % (year,month,day,hour,minutes)
	tweet_time = "%s-%s-%s %s" % (year,month,day,hour)

	return tweet_time

def emit(key,value):
	try:
		print "%s\t%s" % (key,value)
	except UnicodeEncodeError:
		pass

def main():
	#grab all of standard input
	f = sys.stdin.readlines()
	for line in f:
		#load in the line into a python dictionary 
		#(these lines aren't actually json! they are the result of a print of a python dictionary)
		d = ast.literal_eval(line)
		#now the unique code for each mapper begins. above should be standard for all our mappers
		createdAt = d['created_at']
		tweet_time = getTime(createdAt)
		emit(tweet_time,"1")


if __name__ == '__main__':
	main()