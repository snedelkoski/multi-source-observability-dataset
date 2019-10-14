import pandas as pd
import os
import numpy as np

def listLogsProject(projectName):
    """
    :param name: traces, logs, metrics
    :param projectName: One in ['haproxy', 'keystone', 'grafana', 'glance',
                                'mariadb', 'kibana', 'swift', 'nova', 'ceph', 'rally', 'rabbitmq',
                                'placement', 'neutron', 'heat', 'chrony', 'openvswitch', 'cinder', 'horizon']
    :return: List of available logs for the project with projectName;
    """
    path = "/home/jasminb/PycharmProjects/AIOps/2_Copy_Original_Data/openstack_traces_logs_faults/kibana_logs/"+projectName+"/"
    return os.listdir(path)


def readMetrics(nodeID):
    """
    This functions is used to read the metrics data for specific nodes.
    :param nodeID: allowed values [113, 117, 122, 123, 124]
    :return: Data frame of size nx7. Where the 7 columns represent different metrics of interest.
    """
    assert nodeID in [113, 117, 122, 123, 124], str(nodeID) + " invalid node value. Please insert some of the 113, 117, 122, 123, 124 as relevant metrics files."
    path = "/home/jasminb/PycharmProjects/AIOps/2_Copy_Original_Data/openstack_traces_logs_faults/system-metrics/glances_" + str(nodeID) + ".csv"
    return pd.read_csv(path)


def readTraces(operation="boot_delete_api_faults"):
    """
    Valid operations:
    ['network_create_delete', 'boot_delete_api_faults', 'create_delete_image', 'boot_delete_compute_faults_traces', 'cinder_api_faults', 'cinder_compute_faults', 'create_delete_stack'],
    :param operation: valid operation for the trace. It is initialized to boot_delete_api_faults as first operation when the sorting is done by alphabetical order.
    :return:
    """
    path = "/home/jasminb/PycharmProjects/AIOps/2_Copy_Original_Data/openstack_traces_logs_faults/traces_csv/" + operation + ".csv"
    assert operation in ['network_create_delete', 'boot_delete_api_faults', 'create_delete_image', 'boot_delete_compute_faults_traces', 'cinder_api_faults', 'cinder_compute_faults', 'create_delete_stack'], operation + " invalid node value. Please insert some of the set {'network_create_delete.csv', 'boot_delete_api_faults.csv', 'create_delete_image.csv', 'boot_delete_compute_faults_traces.csv', 'cinder_api_faults.csv', 'cinder_compute_faults.csv', 'create_delete_stack.csv'} as relevant trace IDs"
    return pd.read_csv(path)


def readRaw():
    return pd.read_csv("/home/jasminb/PycharmProjects/AIOps/2_Copy_Original_Data/csv_raw.csv")



projectName = "grafana"
nodeID = 113
operation = "boot_delete_api_faults"
#print(listLogsProject(projectName))
#print(readMetrics(nodeID))
#print(readTraces(operation))
#
#data = readRaw(10)