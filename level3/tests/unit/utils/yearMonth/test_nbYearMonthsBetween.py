from app.utils.yearMonth import nbYearMonthsBetween

def test():

    assert nbYearMonthsBetween(2000, 1, 2000, 1) == 1
    assert nbYearMonthsBetween(2000, 1, 2000, 10) == 10
    assert nbYearMonthsBetween(2000, 1, 2001, 10) == 22
    assert nbYearMonthsBetween(2000, 3, 2001, 1) == 11
    