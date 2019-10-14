from reading import *
import matplotlib.pyplot as plt
import os
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
from collections import defaultdict

import matplotlib.ticker

"""
Contains sripts for calculation and plotting of the statistical properties of the "metrics" data.
"""

def plotFeaturesDistributionsMetrics(nodeID, metricsData):
    """
    Function to plot the metrics data for nodeID.
    :param nodeID: The nodeID represents the ID of the node one wants to observe.
    :param metricsData: The metricsData represent the data which distribution we are interested in.
    :return: None. Stores an image of the distribution of the properties in a folder.
    """

    pathToStoreTheImages = "./"

    plt.figure(nodeID, figsize=(12,12))
    plt.rc('xtick', labelsize=13)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=13)  # fontsize of the tick labels
    plt.rc('font', size=13)  # controls default text sizes
    plt.rc('axes', titlesize=13)  # fontsize of the axes title
    plt.rc('axes', labelsize=13)  # fontsize of the x and y labels

    #for cnt, featureName in enumerate(['cpu.user', 'mem.used', 'load.cpucore', 'load.min1', 'load.min5', 'load.min15']):
    for cnt, featureName in enumerate(['cpu.user', 'mem.used', 'load.min1']):
        createSubplot = 230 + cnt + 1
        plt.subplot(createSubplot)
        plt.subplots_adjust(wspace=0.4)
        plt.xlabel(featureName)
        plt.hist(metricsData.loc[:, featureName], bins=100, color="black")

        #if nodeID in [117, 122, 123, 124]:
        #    if featureName == "cpu.user":
        #        plt.xlim((0, 80))

        #    if featureName == "mem.used":
        #        plt.xlim((188463616, 3662356736))

        #    if featureName in ['load.min1', 'load.min5', 'load.min15']:
        #        plt.xlim((0, 3))

        #else:
        #        if featureName == "cpu.user":
        #            plt.xlim((0, 80))

        #        if featureName in ['load.min1', 'load.min5', 'load.min15']:
        #            plt.xlim((0, 17))

    tmpPath = pathToStoreTheImages + str(nodeID) + "_new.pdf"
    #plt.suptitle("Metrics data for node: " + str(nodeID))
    plt.savefig(tmpPath, bbox_inches="tight")
    #cutPDF(tmpPath)
    plt.close()


def caluclateStatisticalProperties(metricData):
    """
     Function calculating statistical Properties of the metricData for a specific node.
    :param nodeID: The nodeID represents the ID of the node one wants to observe.
    :param metricData: The metricsData represent the data which distribution we are interested in.
    :return: To be continued if needed
    """
    d = defaultdict(dict)
    for _, featureName in enumerate(['cpu.user', 'mem.used', 'load.cpucore', 'load.min1', 'load.min5', 'load.min15']):
        d[featureName]["mean"] = np.mean(metricData.loc[:, featureName])
        d[featureName]["median"] = np.median(metricData.loc[:, featureName])
        d[featureName]["std"] = np.std(metricData.loc[:, featureName])
        d[featureName]["min"] = np.min(metricData.loc[:, featureName])
        d[featureName]["max"] = np.max(metricData.loc[:, featureName])
    return d
    #tmpPath = path + str(nodeID) + ".csv"


def cutPDF(filePath):
    """
    Helper function to trim a pdf.
    :param filePath: the Path were the pdf is stored.
    :return:
    """
    pdfRead = PdfFileReader(open(filePath, "rb"))
    page = pdfRead.getPage(0)
    print(page.cropBox.getLowerLeft())
    print(page.cropBox.getLowerRight())
    print(page.cropBox.getUpperLeft())
    print(page.cropBox.getUpperRight())
    lower_right_new_x_coordinate  = 864
    lower_right_new_y_coordinate = 400
    lower_left_new_x_coordinate = 0
    lower_left_new_y_coordinate = 400
    upper_left_new_x_coordinate = 0
    upper_left_new_y_coordinate = 864
    upper_right_new_x_coordinate = 864
    upper_right_new_y_coordinate = 864
    page.mediaBox.lowerRight = (lower_right_new_x_coordinate, lower_right_new_y_coordinate)
    page.mediaBox.lowerLeft = (lower_left_new_x_coordinate, lower_left_new_y_coordinate)
    page.mediaBox.upperRight = (upper_right_new_x_coordinate, upper_right_new_y_coordinate)
    page.mediaBox.upperLeft = (upper_left_new_x_coordinate, upper_left_new_y_coordinate)
    output = PdfFileWriter()
    output.addPage(page)
    with open("113_new.pdf", "wb") as out_f:
        output.write(out_f)

lis = []
for nodeID in [113, 117, 122, 123, 124]:
#for nodeID in [113, 117]:
    metricData = readMetrics(nodeID)
    lis.append(metricData.shape[0])
    plotFeaturesDistributionsMetrics(nodeID, metricData)
    #break


