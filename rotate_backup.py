#!/usr/bin/env python
import sys
import os
import glob
import time

class archive:
    def __init__(self, path):
        self.path = path
        self.time = time.gmtime(os.path.getmtime(path))
        self.year = time.strftime("%Y", self.time)
        self.month = time.strftime("%Y%m", self.time)
        self.week = time.strftime("%Y%W", self.time)
        self.day = time.strftime("%Y%m%d", self.time)
        self.hour = time.strftime("%Y%m%d%H", self.time)
        self.min = time.strftime("%Y%m%d%H%M", self.time)
        self.sec = time.strftime("%Y%m%d%H%M%S", self.time)

    def rm(self):
        print "rm %s" % self.path
        os.remove(self.path)

class binStoreNewest:
    def __init__(self, binNum):
        self.bins = {}
        self.binNum = binNum

    def add(self, id, item):
        if id in self.bins:  # there is a archive for this cluster id
            storedItem = self.bins[id]
            if storedItem.time < item.time:  # item is newer then the stored one
                self.bins[id] = item
        else:
            self.bins[id] = item    # there wasn't archive for this cluster id still now

        keys = self.bins.keys()
        keys.sort()
        for id in keys[:-self.binNum]:  # delete the archives out of scope, keep the last binNum ones
            del self.bins[id]

    def getPaths(self):
        return [item.path for item in self.bins.values()]

def getBinTops(sourceArray, binNum, clusterFunction):
    binStore = binStoreNewest(binNum)
    for item in sourceArray:
        binStore.add(clusterFunction(item), item)
    return binStore.getPaths()

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        files = sys.argv[1:]
    else:
        files = glob.glob("./data/*")

    archives = [archive(filename) for filename in files]

    daily = getBinTops(archives, 7, lambda item: item.day)
    weekly = getBinTops(archives, 4, lambda item: item.week)
    monthly = getBinTops(archives, 12, lambda item: item.month)
    yearly = getBinTops(archives, 10, lambda item: item.year)

    keepPaths = daily + weekly + monthly + yearly

    for item in archives:
        if item.path not in keepPaths:
            item.rm()
