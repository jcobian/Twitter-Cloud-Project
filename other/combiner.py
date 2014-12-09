#!/usr/bin/python
import sys

def main():
	start_day = sys.argv[1]
	end_day = sys.argv[2]
	limit = int(sys.argv[3])
	results = []
	usedKeys = set()
	for line in sys.stdin:
		tokens = line.split("\t")
		key = tokens[0]
		if key not in usedKeys:
			value = int(tokens[1])
			results.append((key,value))
			usedKeys.add(key)
		else:
			print "Error: %s in file more than once" % key
			sys.exit()

	results = sorted(results,key=lambda x:x[1],reverse=True)
	results = results[:limit]
	for rank,tup in enumerate(results):
		print "%s,%s 00:00:00,%s 23:59:59,%s,%s" % (tup[0],start_day,end_day,rank+1,tup[1])


if __name__ == '__main__':
	main()