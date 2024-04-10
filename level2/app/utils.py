from datetime import datetime

def computeMonthsInQuarter(year, quarter):

    startMonth = (quarter - 1) * 3 + 1

    return [ (year, startMonth + monthIndex) for monthIndex in range(3) ]

def computePreviousMonth(year, month):

    if month >= 2:
        return year, month-1
    
    return year-1, 12

# This is a generator that iterates between two given months
def monthsBetween(startYear, startMonth, endYear, endMonth):

    year = startYear
    month = startMonth

    while year < endYear or (year == endYear and month <= endMonth):

        yield year,month

        month += 1

        if month == 13:
            year +=1
            month = 1