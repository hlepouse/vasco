# These are useful functions that deal with year/month tuples
# These operations could have been handled with the datetime library,
# however this lib can only handle dates (not just months), it would make the code less readable

from datetime import datetime

def computeStartEndMonths(quarter):

    startMonth = (quarter - 1) * 3 + 1

    return startMonth, startMonth+2

def computePreviousYearMonth(year, month):

    if month >= 2:
        return year, month-1
    
    return year-1, 12

# This is a generator that iterates between two given months
def yearMonthsBetween(startYear, startMonth, endYear, endMonth):

    year = startYear
    month = startMonth

    while year < endYear or (year == endYear and month <= endMonth):

        yield year,month

        month += 1

        if month == 13:
            year +=1
            month = 1

# Checks if there is at least one month in the provided range
# We don't need to check for the month to be between 1 and 12, because
# this is checked at schema validation
def isYearMonthRangeValid(startYear, startMonth, endYear, endMonth):

    if startYear > endYear:
        return False
    
    if startYear < endYear:
        return True
    
    if startMonth > endMonth:
        return False
    
    return True