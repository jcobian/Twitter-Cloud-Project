#!/usr/bin/python
from sys import stdin

#will sort based on the number and emit in sorted order
def emitInOrder(results,limit=100):
        results = sorted(results,key=lambda x:x[1],reverse=True)
        if limit:
                results = results[:100]
        for rank,tup in enumerate(results):
                emit(tup[0],tup[2],tup[3],rank+1)

def emit(key,startTime,endTime,value):
        print "%s,%s,%s,%s" % (key,startTime,endTime,value)

def main():
        results = []
        oldkey = None
        count = 0
        for line in stdin:
                #line = line.strip()
                arr = line.split("\t")
                emitKey = arr[0].split(";")
                key = emitKey[0]
                startTime = emitKey[1]
                endTime = emitKey[2]
                value = arr[1]
                if not oldkey:
                        oldkey = key
                        count = int(value)
                else:
                        if oldkey == key:
                                count+=1
                        else:
                                results.append((oldkey,count,startTime,endTime))
                                oldkey = key
                                count = int(value)
        results.append((oldkey,count,startTime,endTime))
        emitInOrder(results)

if __name__ == "__main__":
        main()