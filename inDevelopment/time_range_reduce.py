#!/usr/bin/python
from sys import stdin

#will sort based on the number and emit in sorted order
def emitInOrder(results):
        results = sorted(results,key=lambda x:x[0],reverse=False)
        for rank,tup in enumerate(results):
                emit(tup[0],tup[1])

def emit(key,value):
        print "%s,%s" % (key,value)

def main():
        results = []
        oldkey = None
        count = 0
        for line in stdin:
                #line = line.strip()
                arr = line.split("\t")
                key = arr[0]
                value = arr[1]
                if not oldkey:
                        oldkey = key
                        count = int(value)
                else:
                        if oldkey == key:
                                count+=1
                        else:
                                results.append((oldkey,count))
                                oldkey = key
                                count = int(value)
        results.append((oldkey,count))
        emitInOrder(results)

if __name__ == "__main__":
        main()