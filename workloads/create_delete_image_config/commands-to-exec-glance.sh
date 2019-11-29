#!/bin/bash -x
# Restarting glance_api container 10 times and sleep for 2 secs between restarts
for i in {1..1}
do
    echo "Restarting glance-container"
    docker restart glance_api	
done


