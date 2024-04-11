# These are generic computing functions, designed to compute metrics for any range of months
# They are used in quaterly computations
# They cannot be used in monthly computations, because the formulas don't match

from app.utils.YearMonth import YearMonth
from app.utils.YearMonthRange import YearMonthRange
import os

def isDataAvailable(targets, yearMonthRange):

    for yearMonth in yearMonthRange.iterate():

        if targets.get(yearMonth) is None:
            return False
        
    return True

def computeRangeRecurringRevenue(targets, yearMonthRange):

    return targets[yearMonthRange.end]["recurringRevenue"]

def computePreviousRecurringRevenue(targets, yearMonth):

    previousYearMonth = yearMonth.previous()
    previousTarget = targets.get(previousYearMonth)

    if previousTarget is None:
        return float(os.getenv("DEFAULT_PREVIOUS_RECURRING_REVENUE"))
    
    return previousTarget["recurringRevenue"]

# This function must only be called with nbYearMonths > 0
def computeRangeAverageRecurringRevenue(targets, yearMonthRange):

    sumRecurringRevenue = sum([
        targets[yearMonth]["recurringRevenue"]
        for yearMonth in yearMonthRange.iterate()
    ])

    nbYearMonths = yearMonthRange.size()

    # The constructor or YearMonthRange enforces size >= 1, so no problem with division
    return sumRecurringRevenue / nbYearMonths

def computeRangeRate(targets, rateMetric, previousRecurringRevenue, averageRecurringRevenue, yearMonthRange):

    amount = 0

    for yearMonth in yearMonthRange.iterate():

        amount += previousRecurringRevenue * targets[yearMonth][rateMetric]
        previousRecurringRevenue = targets[yearMonth]["recurringRevenue"]

    # In case of average recurring revenue at zero, the rate cannot be computed
    # Do not return some random value : return None, and let the caller decide how to display it
    try:
        rate = round(amount / averageRecurringRevenue, 3)
    except ZeroDivisionError as e:
        rate = None

    return rate

def computeAcquisitionTarget(targets, yearMonth):

    previousRecurringRevenue = computePreviousRecurringRevenue(targets, yearMonth)

    return targets[yearMonth]["recurringRevenue"] - previousRecurringRevenue

def computeRangeAcquisitionTarget(targets, yearMonthRange):

    return sum([
        computeAcquisitionTarget(targets, yearMonth)
        for yearMonth in yearMonthRange.iterate()
    ])

def computeNetRetentionRate(targets, yearMonth):

    targetMonth = targets[yearMonth]

    return 1 - targetMonth["downgradeRate"] + targetMonth["upgradeRate"] - targetMonth["churnRate"]

def computeExpansionTarget(targets, yearMonth):

    netRetentionRate = computeNetRetentionRate(targets, yearMonth)
    previousRecurringRevenue = computePreviousRecurringRevenue(targets, yearMonth)

    return previousRecurringRevenue * (1 - netRetentionRate)

def computeRangeExpansionTarget(targets, yearMonthRange):

    return sum([
        computeExpansionTarget(targets, yearMonth)
        for yearMonth in yearMonthRange.iterate()
    ])

def computeRangeMetrics(targets, yearMonthRange):

    metrics = {}

    nbYearMonths = yearMonthRange.size()
    rateMetricsList = os.getenv("RATE_METRICS").split(",")

    rangePreviousRecurringRevenue = computePreviousRecurringRevenue(targets, yearMonthRange.start)
    averageRecurringRevenue = computeRangeAverageRecurringRevenue(targets, yearMonthRange)

    if nbYearMonths == 1:

        metrics = {
            rateMetric: targets[yearMonthRange.start][rateMetric]
            for rateMetric in rateMetricsList
        }
    else:

        metrics = {
            rateMetric: computeRangeRate(targets, rateMetric, rangePreviousRecurringRevenue, averageRecurringRevenue, yearMonthRange)
            for rateMetric in rateMetricsList
        }

    metrics["recurringRevenue"] = round(computeRangeRecurringRevenue(targets, yearMonthRange), 3)
    metrics["acquisitionTarget"] = round(computeRangeAcquisitionTarget(targets, yearMonthRange), 3)
    metrics["expansionTarget"] = round(computeRangeExpansionTarget(targets, yearMonthRange), 3)

    return metrics

