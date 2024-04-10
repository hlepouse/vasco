import os

def convertPercentToFloat(rate):

    return rate / 100

def preprocessTargets(targetsList):

    targetsDict = {}

    for target in targetsList:

        for targetMetric in os.getenv('RATE_METRICS').split(","):

            target[targetMetric] = convertPercentToFloat(target[targetMetric])

        targetsDict[target["year"], target["month"]] = target

    return targetsDict