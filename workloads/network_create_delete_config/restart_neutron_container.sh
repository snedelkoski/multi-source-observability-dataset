#!/bin/bash +x

#SSH into Wally113 controller and execute commands from commands-to-exec-nova.sh

cat commands-to-exec-neutron.sh | sshpass -p 'rally' ssh rally@wally113.cit.tu-berlin.de
