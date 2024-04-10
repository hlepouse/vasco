from app.utils.yearMonth import isYearMonthRangeValid

def test():

    assert isYearMonthRangeValid(2000, 1, 2000, 2)
    assert isYearMonthRangeValid(2000, 1, 2000, 1)
    assert isYearMonthRangeValid(1999, 2, 2000, 1)
    assert not isYearMonthRangeValid(2001, 1, 2000, 2)
    assert not isYearMonthRangeValid(2000, 2, 2000, 1)