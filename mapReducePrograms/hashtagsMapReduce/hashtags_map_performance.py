#!/usr/bin/python
import sys
import ast
import datetime
import string,re
regex = re.compile('[,.!?;]')
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
		#grab out the actual text of the tweet
		text = d['text']
		#emit the hashtags
		tokens = text.split()
		for word in tokens:
			if word.startswith("#"):
				word = regex.sub('',word)
				if word != "#":
					emit(word.lower(),"1")

if __name__ == '__main__':
	main()