from app.computing import isDataAvailable
from app.utils.YearMonth import YearMonth
from app.utils.YearMonthRange import YearMonthRange

def test():

    targets = {
        YearMonth(2000,1): {}
    }

    assert isDataAvailable(targets, YearMonthRange(YearMonth(2000, 1), YearMonth(2000, 1)))
    assert not isDataAvailable(targets, YearMonthRange(YearMonth(2000, 1), YearMonth(2000, 2)))
