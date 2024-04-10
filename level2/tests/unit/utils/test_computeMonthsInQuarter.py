from app.utils import computeMonthsInQuarter

def test():

    assert computeMonthsInQuarter(2000, 1) == [(2000,1),(2000,2),(2000,3)]