"""
Contains usefull functions for calculating the properties of the Traces data.
"""
from reading import *
from pprint import PrettyPrinter
from collections import defaultdict
import json


def addOnes(dataFrame):
    """
    :param dataFrame: dataFrame representing traces
    :return: dataFrame + newColumn of ones
    """
    dataFrame["ones"] = np.ones(dataFrame.shape[0])
    return dataFrame


def groupCounts(dataFrame):
    pom = dataFrame.loc[:, ["Base_id", "ones"]].groupby(by=["Base_id"]).count()/2
    return  pom


def groupCountsAllFeatures(dataFrame, feature):
    pom = dataFrame.loc[:, [feature, "ones"]].groupby(by=[feature]).count()/2
    return pom


def storeJsons(dic, pathToStore):
    """
    :param dic: dict containing the properties
    :param operation: the operation being executed
    :param pathToStore: should be in form ./Traces/
    :return:
    """
    with open(pathToStore + "Traces_allFeatures.json", "w") as file:
        json.dump(dic, file)


def calculateStats(dataFrame, feature):
    d={}
    d["mean"] = float(list(dataFrame.mean().values)[0])
    d["std"] = float(list(dataFrame.std().values)[0])
    d["median"] = float(list(dataFrame.median().values)[0])
    d["min"] = float(list(dataFrame.min().values)[0])
    d["max"] = float(list(dataFrame.max().values)[0])
    d["quantile05"] = float(list(dataFrame.quantile(0.05).values)[0])
    d["quantile25"] = float(list(dataFrame.quantile(0.25).values)[0])
    d["quantile50"] = float(list(dataFrame.quantile(0.50).values)[0])
    d["quantile75"] = float(list(dataFrame.quantile(0.75).values)[0])
    d["quantile95"] = float(list(dataFrame.quantile(0.95).values)[0])
    d["numberUniqueValues"] = dataFrame.shape[0]

    return d

def tracesStats():
    """
    :return: creates .json files for the stats of all of the operations.
    """
    operationName = ['boot_delete_api_faults', 'boot_delete_compute_faults_traces', 'cinder_api_faults', 'cinder_compute_faults',   'create_delete_image',  'create_delete_stack', 'network_create_delete',]
    dic = defaultdict(dict)
    dic1 = defaultdict(list)
    for operation in operationName:
        first = readTraces(operation)
        pom1 = addOnes(first)
        pom1 = pom1.drop(["Unnamed: 0"], axis=1)
        dic1[operation] = pom1
        for feature in pom1.columns[:-1]:
            pom2 = groupCountsAllFeatures(pom1, feature)
            pom3 = calculateStats(pom2, feature)
            dic[operation][feature] = pom3

    storeJsons(dic, "./")

        #lista.append(dic)


def propertiesPerFeature():
    """

    :return: DataFrame containing the number of calls per operation on each type of calls. [rpc, wsgi and vif]
    """
    li = []
    operationName = ['boot_delete_api_faults', 'boot_delete_compute_faults_traces', 'cinder_api_faults',
                     'cinder_compute_faults', 'create_delete_image', 'create_delete_stack', 'network_create_delete', ]
    for operation in operationName:
        print("###########")
        print(operation)
        print("###########")
        first = readTraces(operation)
        oi = pd.value_counts(first.Name)
        dictionary = {}
        d = {}
        typesOfCalls = ["rpc", "wsgi", "vif", "driver"]
        for typeOfCall in typesOfCalls:
            flag = True
            for ind, x in enumerate(list(oi.index)):
                if typeOfCall in x:
                    if flag == True:
                        print("The operation {} has {} calls of type {} that number: {}".format(operation, typeOfCall, x, oi.loc[x]))

                        #li.append(oi.loc[x])
                        d[typeOfCall] = oi.loc[x]
                        flag = False
                        #q = np.array(li)
                    else:
                        flag = True
        pomm = list(d.keys())
        if len(pomm) != 4:
            if "rpc" not in pomm:
                d["rpc"] = 0
            if "wsgi" not in pomm:
                d["wsgi"] = 0
            if "vif" not in pomm:
                d["vif"] = 0
            if "driver" not in pomm:
                d["driver"] = 0
        dictionary[operation] = d
        li.append(pd.DataFrame(dictionary))
    return pd.concat(li, axis=1)
"""
    for operation in operationName:
        print("#######################################################")
        print("#######################################################")
        print("The mean number of calls for operation {} type of call {} is {}".format(operation, typeOfCall, np.mean(q)))
        print("The std per number of calls for operation {} type of call {} is {}".format(operation, typeOfCall, np.std(q)))
        print("The median number of calls for operation {} type of call {} is {}".format(operation, typeOfCall, np.median(q)))
        print("The max number of calls for operation {} type of call {} is {}".format(operation, typeOfCall, np.max(q)))
        print("The min number of calls for operation {} type of call {} is {}".format(operation, typeOfCall, np.min(q)))
        print("#######################################################")
        print("#######################################################")
"""
tracesStats()
a = propertiesPerFeature()