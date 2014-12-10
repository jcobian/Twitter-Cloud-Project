#!/usr/bin/python
from sys import stdin

#will sort based on the number and emit in sorted order
def emitInOrder(results,limit=100):
        results = sorted(results,key=lambda x:x[1],reverse=True)
        if limit:
                results = results[:100]
        for rank,tup in enumerate(results):
                emit(tup[0],tup[1])

def emit(key,count):
        print "%s\t%s" % (key,count)

def main():
        results = []
        oldkey = None
        count = 0
        for line in stdin:
                arr = line.split("\t")
                key = arr[0]
                value = arr[1]
                #first time through the file
                if not oldkey:
                        oldkey = key
                        count = int(value)
                else:
                        #still on the old key so add to sum
                        if oldkey == key:
                                count+=int(value)
                        else:
                                #got a  new key so append the old key and the old count and set to this rows
                                results.append((oldkey,count))
                                oldkey = key
                                count = int(value)
        #add the last key and its last count
        results.append((oldkey,count))
        #emit the keys in sorted order by the count
        emitInOrder(results)

if __name__ == "__main__":
        main()