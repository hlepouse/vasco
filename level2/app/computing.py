# These are generic computing functions, designed to compute metrics for any range of months
# They are used in quaterly computations
# They cannot be used in monthly computations, because the formulas don't match

from app.utils.yearMonth import yearMonthsBetween, computePreviousYearMonth
import os

def isDataAvailable(targets, startYear, startMonth, endYear, endMonth):

    for year,month in yearMonthsBetween(startYear, startMonth, endYear, endMonth):

        if targets.get((year,month)) is None:
            return False
        
    return True

def computeRecurringRevenue(targets, startYear, startMonth, endYear, endMonth):

    return targets[(endYear,endMonth)]["recurringRevenue"]

def computePreviousRecurringRevenue(targets, year, month):

    previousYear, previousMonth = computePreviousYearMonth(year, month)
    previousTarget = targets.get((previousYear, previousMonth))

    if previousTarget is None:
        return float(os.getenv("DEFAULT_PREVIOUS_RECURRING_REVENUE"))
    
    return previousTarget["recurringRevenue"]

# This function must only be called on a valid range
def computeAverageRecurringRevenue(targets, startYear, startMonth, endYear, endMonth):

    countMonths = 0
    sumRecurringRevenue = 0

    for year,month in yearMonthsBetween(startYear, startMonth, endYear, endMonth):

        countMonths += 1
        sumRecurringRevenue += targets[year,month]["recurringRevenue"]

    # We don't check for division by zero, because the range is supposed to be valid
    return sumRecurringRevenue / countMonths

def computeRate(targets, rateMetric, averageRecurringRevenue, startYear, startMonth, endYear, endMonth):

    amount = 0
    previousRecurringRevenue = computePreviousRecurringRevenue(targets, startYear, startMonth)

    for year,month in yearMonthsBetween(startYear, startMonth, endYear, endMonth):

        amount += previousRecurringRevenue * targets[year,month][rateMetric]
        previousRecurringRevenue = targets[year,month]["recurringRevenue"]

    # In case of average recurring revenue at zero, the rate cannot be computed
    # Do not return some random value : return None, and let the frontend decide how to display it
    try:
        rate = amount / averageRecurringRevenue
    except ZeroDivisionError as e:
        rate = None

    return rate

def computeMetrics(targets, startYear, startMonth, endYear, endMonth):

    averageRecurringRevenue = computeAverageRecurringRevenue(targets, startYear, startMonth, endYear, endMonth)

    metrics = {
        rateMetric: computeRate(targets, rateMetric, averageRecurringRevenue, startYear, startMonth, endYear, endMonth)
        for rateMetric in os.getenv("RATE_METRICS").split(",")
    }

    metrics["recurringRevenue"] = computeRecurringRevenue(targets, startYear, startMonth, endYear, endMonth)

    return metrics