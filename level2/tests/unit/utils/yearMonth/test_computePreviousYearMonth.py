from app.utils.yearMonth import computePreviousYearMonth

def test():

    assert computePreviousYearMonth(2000, 1) == (1999,12)
    assert computePreviousYearMonth(2000, 2) == (2000,1)