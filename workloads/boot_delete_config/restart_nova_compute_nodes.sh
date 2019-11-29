#!/bin/bash +x

#SSH into compute nodes and execute commands from commands-to-exec-nova-compute.sh
cat commands-to-exec-nova-compute.sh | sshpass -p 'rally' ssh rally@wally117.cit.tu-berlin.de &
cat commands-to-exec-nova-compute.sh | sshpass -p 'rally' ssh rally@wally122.cit.tu-berlin.de &
cat commands-to-exec-nova-compute.sh | sshpass -p 'rally' ssh rally@wally124.cit.tu-berlin.de &
cat commands-to-exec-nova-compute.sh | sshpass -p 'rally' ssh rally@wally123.cit.tu-berlin.de &
cat commands-to-exec-nova-compute.sh | sshpass -p 'rally' ssh rally@wally113.cit.tu-berlin.de
