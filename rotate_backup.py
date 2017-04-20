#!/usr/bin/env python
import sys
import os
import glob
import time

class archive:
    def __init__(self, path):
        self.path = path
        self.sec  = int(time.time() - os.path.getmtime(path))
        self.min  = self.sec / 60
        self.hour = self.min / 60
        self.day  = self.hour / 24
        self.week = self.day / 7

    def rm(self):
        print "rm %s" % self.path
        os.remove(self.path)

def getBinHead(array, binNum, grouping_function):
    bins = {}

    for a in array:
        group = grouping_function(a)
        if group in bins:  bins[group].append(a)
        else:              bins[group] = [a]

    binkeys = bins.keys()
    binkeys.sort() # sorting in youngest->oldest order
    binkeys = binkeys[:binNum] # keep these bins

    keep = [bins[key] for key in binkeys]

    def sec(item):
        return item.sec

    tops = [min(item, key=sec) for item in keep]
    return set(tops)


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        files = sys.argv[1:]
    else:
        files = glob.glob("./data/*")

    archives = [archive(filename) for filename in files]

    keep_daily = getBinHead(archives, 7, lambda x: x.day)
    keep_weekly = getBinHead(archives, 4, lambda x: x.week)
    keep_all = keep_daily.union(keep_weekly)
    remove_files= set(archives).difference(keep_all)

    for item in remove_files:
        item.rm()


