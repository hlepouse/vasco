from app.utils.YearMonthRange import YearMonthRange
from app.utils.YearMonth import YearMonth
import pytest

def testInit():

    YearMonthRange(YearMonth(1999,12), YearMonth(2000,1))
    YearMonthRange(YearMonth(2000,1), YearMonth(2000,1))

    with pytest.raises(ValueError):
        YearMonthRange(YearMonth(2000,1), YearMonth(1999,12))

def testSize():

    assert YearMonthRange(YearMonth(2000,1), YearMonth(2000,1)).size() == 1
    assert YearMonthRange(YearMonth(2000,1), YearMonth(2000,10)).size() == 10
    assert YearMonthRange(YearMonth(2000,1), YearMonth(2001,10)).size() == 22
    assert YearMonthRange(YearMonth(2000,3), YearMonth(2001,1)).size() == 11

def testIterate():

    list(YearMonthRange(YearMonth(1999,11), YearMonth(2000,2)).iterate()) == [
        YearMonth(1999,11),
        YearMonth(1999,12),
        YearMonth(2000,1),
        YearMonth(2000,2)
    ]

def testFromQuarter():

    assert YearMonthRange.fromQuarter(2000, 2) == YearMonthRange(YearMonth(2000,4), YearMonth(2000,6))
