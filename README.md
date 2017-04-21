# rotate_backup
Simple python script for clean backup based on backup ages.

    getBinTops(sourceArray, binNum, clusterFunction)

pushes the items of the sourceArray into binNum bins.
Each bin can store only one item, that is the newest element with the biggest item.time value.
The bins are identified by the clusterFunction(item) method.


    daily = getBinTops(archives, 7, lambda item: item.day)
    weekly = getBinTops(archives, 4, lambda item: item.week)
    monthly = getBinTops(archives, 12, lambda item: item.month)
    yearly = getBinTops(archives, 10, lambda item: item.year)

    keepPaths = daily + weekly + monthly + yearly


# testing
    ./test.sh
It will create a bunch of 0 byte long tar.gz archives with different ages in the data folder.

# Run the cleanup
    ./rotate_backup.py

# Result

    jjuhasz@jjuhasz-ThinkPad-L560:~/rotate_backup$ ls -lt data
    összesen 0
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 ápr   20 09:11 backup_1.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 ápr   19 09:11 backup_2.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 ápr   18 09:11 backup_3.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 ápr   17 09:11 backup_4.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 ápr   16 09:11 backup_5.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 ápr   15 09:11 backup_6.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 ápr   14 09:11 backup_7.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 ápr    9 09:11 backup_12.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 ápr    2 09:11 backup_19.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 márc  31 09:11 backup_21.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 febr  28 08:11 backup_52.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 jan   31 08:11 backup_80.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 dec   31 08:11 backup_111.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 nov   30 08:11 backup_142.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 okt   31 08:11 backup_172.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 szept 30  2016 backup_203.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 aug   31  2016 backup_233.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 júl   31  2016 backup_264.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 jún   30  2016 backup_295.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 máj   31  2016 backup_325.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 dec   31  2015 backup_477.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 dec   31  2014 backup_842.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 dec   31  2013 backup_1207.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 dec   31  2012 backup_1572.tar.gz
    -rw-rw-r-- 1 jjuhasz jjuhasz 0 dec   31  2011 backup_1938.tar.gz
    
