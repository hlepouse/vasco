from app.utils.yearMonth import previousYearMonth

def test():

    assert previousYearMonth(2000, 1) == (1999,12)
    assert previousYearMonth(2000, 2) == (2000,1)