#!/usr/bin/env bash
for i in `seq 100`; do touch -d "-$i days" "data/backup_$i.tar.gz"; done
