from app.utils import monthsBetween

def test():

    assert list(monthsBetween(1999,11,2000,2)) == [(1999,11),(1999,12),(2000,1),(2000,2)]