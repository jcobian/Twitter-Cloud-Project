import json
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

		#grab out the actual text of the tweet
		text = d['text']
		#emit the hashtags
		tokens = text.split()
		for word in tokens:
			if word.startswith("#"):
				emit(word,"1")


if __name__ == '__main__':
	main()