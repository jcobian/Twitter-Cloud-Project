#!/usr/bin/python
#TODO: HOW WILL THIS WORK? WILL WE EMIT TWEET ID AND LAT LONG?
import sys
import ast

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

		#coordiantes is a dictionary
		coordinates = d['coordinates']
		#createdAt = d['created_at']
		if coordinates:
			latLng = coordinates['coordinates'] #this is a list of 2 elements: lat and long
			if latLng:
				#print "yes\t1"
				lat = latLng[0]
				longi = latLng[1]
				emitKey = "%s,%s" % (lat,longi)
				emit(emitKey,1)
			#else:
				#print "no\t1"
		#else:
			#print "no\t1"



if __name__ == '__main__':
	main()