# These are generic computing functions, designed to compute metrics for any range of months
# They are used in quaterly computations
# They cannot be used in monthly computations, because the formulas don't match

from app.utils.yearMonth import yearMonthsBetween, previousYearMonth, nbYearMonthsBetween
import os

def isDataAvailable(targets, startYear, startMonth, endYear, endMonth):

    for year,month in yearMonthsBetween(startYear, startMonth, endYear, endMonth):

        if targets.get((year,month)) is None:
            return False
        
    return True

def computeRangeRecurringRevenue(targets, startYear, startMonth, endYear, endMonth):

    return targets[(endYear,endMonth)]["recurringRevenue"]

def computePreviousRecurringRevenue(targets, year, month):

    previousYear, previousMonth = previousYearMonth(year, month)
    previousTarget = targets.get((previousYear, previousMonth))

    if previousTarget is None:
        return float(os.getenv("DEFAULT_PREVIOUS_RECURRING_REVENUE"))
    
    return previousTarget["recurringRevenue"]

# This function must only be called with nbYearMonths > 0
def computeRangeAverageRecurringRevenue(targets, nbYearMonths, startYear, startMonth, endYear, endMonth):

    sumRecurringRevenue = sum([
        targets[year,month]["recurringRevenue"]
        for year,month in yearMonthsBetween(startYear, startMonth, endYear, endMonth)
    ])

    # We don't check for division by zero, because nbYearMonths > 0
    return sumRecurringRevenue / nbYearMonths

def computeRangeRate(targets, rateMetric, previousRecurringRevenue, averageRecurringRevenue, startYear, startMonth, endYear, endMonth):

    amount = 0

    for year,month in yearMonthsBetween(startYear, startMonth, endYear, endMonth):

        amount += previousRecurringRevenue * targets[year,month][rateMetric]
        previousRecurringRevenue = targets[year,month]["recurringRevenue"]

    # In case of average recurring revenue at zero, the rate cannot be computed
    # Do not return some random value : return None, and let the caller decide how to display it
    try:
        rate = round(amount / averageRecurringRevenue, 3)
    except ZeroDivisionError as e:
        rate = None

    return rate

def computeAcquisitionTarget(targets, year, month):

    previousRecurringRevenue = computePreviousRecurringRevenue(targets, year, month)

    return targets[year,month]["recurringRevenue"] - previousRecurringRevenue

def computeRangeAcquisitionTarget(targets, startYear, startMonth, endYear, endMonth):

    return sum([
        computeAcquisitionTarget(targets, year, month)
        for year,month in yearMonthsBetween(startYear, startMonth, endYear, endMonth)
    ])

def computeNetRetentionRate(targets, year, month):

    targetMonth = targets[year,month]

    return 1 - targetMonth["downgradeRate"] + targetMonth["upgradeRate"] - targetMonth["churnRate"]

def computeExpansionTarget(targets, year, month):

    netRetentionRate = computeNetRetentionRate(targets, year, month)
    previousRecurringRevenue = computePreviousRecurringRevenue(targets, year, month)

    return previousRecurringRevenue * (1 - netRetentionRate)

def computeRangeExpansionTarget(targets, startYear, startMonth, endYear, endMonth):

    return sum([
        computeExpansionTarget(targets, year, month)
        for year,month in yearMonthsBetween(startYear, startMonth, endYear, endMonth)
    ])

def computeRangeMetrics(targets, startYear, startMonth, endYear, endMonth):

    metrics = {}

    nbYearMonths = nbYearMonthsBetween(startYear, startMonth, endYear, endMonth)
    rateMetricsList = os.getenv("RATE_METRICS").split(",")

    rangePreviousRecurringRevenue = computePreviousRecurringRevenue(targets, startYear, startMonth)
    averageRecurringRevenue = computeRangeAverageRecurringRevenue(targets, nbYearMonths, startYear, startMonth, endYear, endMonth)

    if nbYearMonths == 1:

        metrics = {
            rateMetric: targets[startYear, startMonth][rateMetric]
            for rateMetric in rateMetricsList
        }
    else:

        metrics = {
            rateMetric: computeRangeRate(targets, rateMetric, rangePreviousRecurringRevenue, averageRecurringRevenue, startYear, startMonth, endYear, endMonth)
            for rateMetric in rateMetricsList
        }

    metrics["recurringRevenue"] = round(computeRangeRecurringRevenue(targets, startYear, startMonth, endYear, endMonth), 3)
    metrics["acquisitionTarget"] = round(computeRangeAcquisitionTarget(targets, startYear, startMonth, endYear, endMonth), 3)
    metrics["expansionTarget"] = round(computeRangeExpansionTarget(targets, startYear, startMonth, endYear, endMonth), 3)

    return metrics

