#!/bin/bash -x
# Restarting neutron containers and sleep for 25 secs between start and stop
for i in {1}
do
    echo "Restarting neutron-containers"
    docker stop neutron_metadata_agent &
    docker stop neutron_l3_agent &
    docker stop neutron_dhcp_agent &
    docker stop neutron_openvswitch_agent &
    docker stop neutron_openvswitch_agent &
    docker stop neutron_server
    sleep 0.1
    docker start neutron_metadata_agent &
    docker start neutron_l3_agent &
    docker start neutron_dhcp_agent &
    docker start neutron_openvswitch_agent &
    docker start neutron_openvswitch_agent &
    docker start neutron_server
done
