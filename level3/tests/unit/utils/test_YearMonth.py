from app.utils.YearMonth import YearMonth
import pytest

def testInit():

    YearMonth(2000,1)

    with pytest.raises(ValueError):
        YearMonth(0,1)

    with pytest.raises(ValueError):
        YearMonth(2000,0)

def testComparison():

    assert YearMonth(2000,1) == YearMonth(2000,1)
    assert YearMonth(2000,1) < YearMonth(2000,2)
    assert YearMonth(2000,1) <= YearMonth(2000,1)
    assert YearMonth(1999,12) < YearMonth(2000,1)

def testPrevious():

    assert YearMonth(2000,1).previous() == YearMonth(1999,12)

def testNext():

    assert YearMonth(1999,12).next() == YearMonth(2000,1)