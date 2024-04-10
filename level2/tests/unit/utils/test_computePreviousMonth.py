from app.utils import computePreviousMonth

def test():

    assert computePreviousMonth(2000, 1) == (1999,12)
    assert computePreviousMonth(2000, 2) == (2000,1)