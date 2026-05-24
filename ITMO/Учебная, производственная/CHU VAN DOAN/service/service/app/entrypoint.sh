#!/bin/sh

while true; do
    /usr/bin/env socat -T 120 tcp-l:10001,reuseaddr,fork exec:"/app/service.sh"
done
