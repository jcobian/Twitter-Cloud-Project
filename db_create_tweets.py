#!/usr/bin/python
#TODO: CHANGE SO EMITTING TWEETID AND THE HASHTAG
import sys
import ast

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

	print "ERROR NO MATCHING DATE"
	sys.exit()

def reformatTime(time):
	tokens = time.split(" ")
	year = tokens[5]
	hour = tokens[3].split(":")[0]
	minutes = tokens[3].split(":")[1]
	seconds = tokens[3].split(":")[2]
	month = getMonthNum(tokens[1])
	day = tokens[2]
	if len(day)==1:
		day = "0"+day
	return "%s-%s-%s %s:%s:%s" % (year,month,day,hour,minutes,seconds)

def main():
	#grab all of standard input
	f = open("crimea-data-full.txt")
	withLats= open("withLats.txt","w")
	noLats = open("noLats.txt","w")
	#hashtags = open("Hashtag.txt","w")
	#media = open("Media.txt","w")
	#keyword = open("Keyword.txt","w")
	#tweet_id = 0
	for line in f:
		#tweet_id+=1
		#load in the line into a python dictionary 
		#(these lines aren't actually json! they are the result of a print of a python dictionary)
		d = ast.literal_eval(line)
		tweet_id = d['id']
		lat = None
		longi = None
		time = d['created_at']
		time2 = reformatTime(time)
		retweets = d['retweet_count']
		favorites = d['favorite_count']
		#coordiantes is a dictionary
		coordinates = d['coordinates']
		if coordinates:
			latLng = coordinates['coordinates'] #this is a list of 2 elements: lat and long
			if latLng:
				lat = latLng[0]
				longi = latLng[1]

		if lat and longi:
			withLats.write("%s,%s,%s,%s,%s,%s\n" % (tweet_id,lat,longi,time2,retweets,favorites))
			#print "%s,%s,%s,%s,%s,%s\n" % (tweetID,lat,longi,time,retweets,favorites)
		else:
			noLats.write("%s,%s,%s,%s\n" % (tweet_id,time2,retweets,favorites))
			#print "%s,%s,%s,%s\n" % (tweetID,time,retweets,favorites)


		'''
		###hashtag 
		#grab out the actual text of the tweet
		text = d['text']

		#emit the hashtags
		tokens = text.split()
		for word in tokens:
			try:
				if word.startswith("#"):
					hashtags.write("%s,%s\n" % (tweet_id,word.lower()))
				elif word.startswith("pic"):
					media.write("%s,%s,%s\n" % (tweet_id,word,"Image"))
				elif word.startswith("http") or word.startswith("bit.ly"):
					media.write("%s,%s,%s\n" % (tweet_id,word,"Link"))
				elif word.isalpha():
					keyword.write("%s,%s\n" % (tweet_id,word))
			except UnicodeEncodeError:
				pass

		'''


	withLats.close()
	noLats.close()
	#hashtags.close()
	#media.close()
	#keyword.close()
	f.close()
				


if __name__ == '__main__':
	main()