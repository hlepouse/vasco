def convertPercentToFloat(rate):

    return rate / 100

def isRateKey(key):

    return key.endswith("Rate")

def preprocessTargets(targetsList):

    targetsDict = {}

    for target in targetsList:

        for targetKey in target.keys():

            if isRateKey(targetKey):
                target[targetKey] = convertPercentToFloat(target[targetKey])

        targetsDict[target["year"], target["month"]] = target

    return targetsDict