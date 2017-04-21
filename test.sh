#!/usr/bin/env bash
for i in `seq 2000`; do touch -d "-$i days" "data/backup_$i.tar.gz"; done
