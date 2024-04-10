from app.preprocessing import isRateKey

def testValidRateKey():

    assert isRateKey("churnRate")

def testInvalidRateKey():

    assert not isRateKey("accurate")
    assert not isRateKey("myRateKey")