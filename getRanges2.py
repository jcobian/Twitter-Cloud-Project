import datetime
import sys 
GAP_SIZE_DAYS = 7
def main():
	f = sys.stdin.readlines()
	count = 0
	intervals = []
	start_day = datetime.date(2014,02,19) 
	end_day = datetime.date(2014,04,9)
	i=0
	while True:
		newDate = start_day+datetime.timedelta(days=i*GAP_SIZE_DAYS)
		intervals.append(newDate)
		if newDate > end_day:
			break
		i+=1

	intervalsLen = len(intervals)
	#print intervals
	#print len(intervals)
	#sys.exit()
	nextIndex = 1
	nextInterval = intervals[nextIndex]
	count = 0
	start_day = f[0].split(",")[0]
	for index,line in enumerate(f):
		tokens = line.split(",")
		dateStr = tokens[0].split()[0]
		year = int(dateStr.split("-")[0])	
		month = int(dateStr.split("-")[1])	
		day = int(dateStr.split("-")[2])	
		currentDay = datetime.date(year,month,day)
		if currentDay == nextInterval:
			end_day = f[index-1].split(",")[0]
			print "%s:00 to %s:59 \t%s" % (start_day,end_day,count)
			start_day = tokens[0]
			count = int(tokens[1])
			nextIndex+=1
			if nextIndex < intervalsLen:
				nextInterval = intervals[nextIndex]
		else:
			count+=int(tokens[1])
	end_day = f[len(f)-1].split(",")[0]
	print "%s:00 to %s:59 \t%s" % (start_day,end_day,count)
			
if __name__ == '__main__':
	main()
