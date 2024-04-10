from app.computing import isDataAvailable

def test():

    targets = {
        (2000,1): {}
    }

    assert isDataAvailable(targets, 2000, 1, 2000, 1)
    assert not isDataAvailable(targets, 2000, 1, 2000, 2)
