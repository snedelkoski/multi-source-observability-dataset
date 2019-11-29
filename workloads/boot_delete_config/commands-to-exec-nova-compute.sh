#!/bin/bash -x
# Restarting nova_api container 5 times and sleep for 10 secs between restarts

for i in {1..2}
do
    echo "Restarting nova-container"
    docker stop nova_compute
    sleep 15
    docker start nova_compute
done


