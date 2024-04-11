# This is a generic computing class, designed to compute metrics for any range of months

from app.utils.YearMonth import YearMonth
from app.utils.YearMonthRange import YearMonthRange

class Computer:

    @staticmethod
    def convertPercentToFloat(rate):

        return rate / 100

    def preprocessTargets(self, targetsList):

        targetsDict = {}

        for target in targetsList:

            for targetMetric in self.rateMetrics:

                target[targetMetric] = Computer.convertPercentToFloat(target[targetMetric])

            yearMonth = YearMonth(target["year"], target["month"])

            del target["year"]
            del target["month"]

            targetsDict[yearMonth] = target

        return targetsDict

    # Constructor of the class
    # The preprocessing of data is performed here
    # The default values are only there to make unit tests more readable
    def __init__(self, targetsList, rateMetrics = [], defaultPreviousRecurringRevenue = 0):

        self.rateMetrics = rateMetrics
        self.defaultPreviousRecurringRevenue = defaultPreviousRecurringRevenue
        self.targets = self.preprocessTargets(targetsList)

    def isDataAvailable(self, yearMonthRange):

        for yearMonth in yearMonthRange.iterate():

            if self.targets.get(yearMonth) is None:
                return False
            
        return True

    def computeRangeRecurringRevenue(self, yearMonthRange):

        return self.targets[yearMonthRange.end]["recurringRevenue"]

    def computePreviousRecurringRevenue(self, yearMonth):

        previousYearMonth = yearMonth.previous()
        previousTarget = self.targets.get(previousYearMonth)

        if previousTarget is None:
            return self.defaultPreviousRecurringRevenue
        
        return previousTarget["recurringRevenue"]

    def computeRangeAverageRecurringRevenue(self, yearMonthRange):

        sumRecurringRevenue = sum([
            self.targets[yearMonth]["recurringRevenue"]
            for yearMonth in yearMonthRange.iterate()
        ])

        nbYearMonths = yearMonthRange.size()

        # The constructor or YearMonthRange enforces size >= 1, so no problem with division
        return sumRecurringRevenue / nbYearMonths

    def computeRangeRate(self, rateMetric, previousRecurringRevenue, averageRecurringRevenue, yearMonthRange):

        amount = 0

        for yearMonth in yearMonthRange.iterate():

            amount += previousRecurringRevenue * self.targets[yearMonth][rateMetric]
            previousRecurringRevenue = self.targets[yearMonth]["recurringRevenue"]

        # In case of average recurring revenue at zero, the rate cannot be computed
        # Do not return some random value : return None, and let the caller decide how to display it
        try:
            rate = round(amount / averageRecurringRevenue, 3)
        except ZeroDivisionError as e:
            rate = None

        return rate

    def computeAcquisitionTarget(self, yearMonth):

        previousRecurringRevenue = self.computePreviousRecurringRevenue(yearMonth)

        return self.targets[yearMonth]["recurringRevenue"] - previousRecurringRevenue

    def computeRangeAcquisitionTarget(self, yearMonthRange):

        return sum([
            self.computeAcquisitionTarget(yearMonth)
            for yearMonth in yearMonthRange.iterate()
        ])

    def computeNetRetentionRate(self, yearMonth):

        targetMonth = self.targets[yearMonth]

        return 1 - targetMonth["downgradeRate"] + targetMonth["upgradeRate"] - targetMonth["churnRate"]

    def computeExpansionTarget(self, yearMonth):

        netRetentionRate = self.computeNetRetentionRate(yearMonth)
        previousRecurringRevenue = self.computePreviousRecurringRevenue(yearMonth)

        return previousRecurringRevenue * (1 - netRetentionRate)

    def computeRangeExpansionTarget(self, yearMonthRange):

        return sum([
            self.computeExpansionTarget(yearMonth)
            for yearMonth in yearMonthRange.iterate()
        ])

    def computeRangeMetrics(self, yearMonthRange):

        metrics = {}

        nbYearMonths = yearMonthRange.size()

        rangePreviousRecurringRevenue = self.computePreviousRecurringRevenue(yearMonthRange.start)
        averageRecurringRevenue = self.computeRangeAverageRecurringRevenue(yearMonthRange)

        if nbYearMonths == 1:

            metrics = {
                rateMetric: self.targets[yearMonthRange.start][rateMetric]
                for rateMetric in self.rateMetrics
            }
        else:

            metrics = {
                rateMetric: self.computeRangeRate(rateMetric, rangePreviousRecurringRevenue, averageRecurringRevenue, yearMonthRange)
                for rateMetric in self.rateMetrics
            }

        metrics["recurringRevenue"] = round(self.computeRangeRecurringRevenue(yearMonthRange), 3)
        metrics["acquisitionTarget"] = round(self.computeRangeAcquisitionTarget(yearMonthRange), 3)
        metrics["expansionTarget"] = round(self.computeRangeExpansionTarget(yearMonthRange), 3)

        return metrics

