# These are all functions necessary to process the data file at application start

import os

def convertPercentToFloat(rate):

    return rate / 100

def preprocessTargets(targetsList):

    targetsDict = {}

    for target in targetsList:

        for targetMetric in os.getenv('RATE_METRICS').split(","):

            target[targetMetric] = convertPercentToFloat(target[targetMetric])

        year = target["year"]
        month = target["month"]

        del target["year"]
        del target["month"]

        targetsDict[year, month] = target

    return targetsDict