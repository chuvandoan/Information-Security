#!/bin/bash
> process_log.txt
for i in {1..60}; do
    echo "$(date +%s) $(ps -e | wc -l)" >> process_log.txt
    sleep 1
done
