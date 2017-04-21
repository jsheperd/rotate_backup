# rotate_backup
Simple python script for clean backup based on backup ages.

    getBinTops(sourceArray, binNum, clusterFunction)

pushes the items of the sourceArray into binNum bins.
Each bin can store only one item, that is the newest element wth the biggest item.time value.
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
