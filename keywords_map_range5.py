#!/usr/bin/python
import sys
import ast
import datetime
START_TIME="2014-03-19 00:00:00"  
END_TIME = "2014-03-25 23:59:59"
start_time_date = datetime.datetime.strptime(START_TIME, "%Y-%m-%d %H:%M:%S").date()
end_time_date = datetime.datetime.strptime(END_TIME, "%Y-%m-%d %H:%M:%S").date()
def inTimeRange(created_at):
	tokens = created_at.split()
	year = tokens[5]
	month = tokens[1]
	day = tokens[2]
	clocktime = tokens[3].split(":")
	hour = clocktime[0]
	minutes = clocktime[1]
	secs = clocktime[2]
	tweet_time = "%s-%s-%s %s:%s:%s" % (year,month,day,hour,minutes,secs)
	tweet_time_date = datetime.datetime.strptime(tweet_time, "%Y-%b-%d %H:%M:%S").date()
	if tweet_time_date > start_time_date and tweet_time_date < end_time_date:
		return True

	return False
def emit(key,value):
	try:
		print "%s\t%s" % (key,value)
	except UnicodeEncodeError:
		pass

def main():
	#grab all of standard input
	for line in sys.stdin:
		#load in the line into a python dictionary 
		#(these lines aren't actually json! they are the result of a print of a python dictionary)
		d = ast.literal_eval(line)
		createdAt = d['created_at']
		if not inTimeRange(createdAt):
			continue
			
		#grab out the actual text of the tweet
		text = d['text']
		#emit the hashtags
		tokens = text.split()
		for word in tokens:
			if word.isalpha() and len(word)>3:
				emit(word,"1")



if __name__ == '__main__':
	main()