#!/usr/bin/env python
import sys
import os
import glob
import time

class archive:
    # The archive class represent an archive media with its age related parameters
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
        # remove the archive from the filesystem
        print "rm %s" % self.path
        os.remove(self.path)

class binStoreNewest:
    # class to store binNum binStores in younger to older order
    # each binstore represent an archive, that is the youngest one of its group
    def __init__(self, binNum):
        self.bins = {}
        self.binNum = binNum

    def add(self, id, item):
        # add a new archive to the clustering
        if id in self.bins:  # there is an archive from this group already
            storedItem = self.bins[id]
            if storedItem.time < item.time:  # act item is newer then the stored one,
                self.bins[id] = item  # replace that
        else:
            self.bins[id] = item    # there wasn't archive for this group till now

        keys = self.bins.keys()
        keys.sort()
        for id in keys[:-self.binNum]:  # keep the binNum newest ones
            del self.bins[id]

    def getPaths(self):
        return [item.path for item in self.bins.values()]

def getBinTops(sourceArray, binNum, clusterFunction):
    # Create groups from the archives by the clusterFunction
    # Return with the newest archives from each group for the newset binNum groups
    binStore = binStoreNewest(binNum)
    for item in sourceArray:
        binStore.add(clusterFunction(item), item)
    return binStore.getPaths()

if __name__ == '__main__':
    # Example usage
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
