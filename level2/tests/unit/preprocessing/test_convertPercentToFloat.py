from app.preprocessing import convertPercentToFloat

def testValidConversion():

    assert convertPercentToFloat(-50) == -0.5
    assert convertPercentToFloat(0) == 0
    assert convertPercentToFloat(50) == 0.5
    assert convertPercentToFloat(100) == 1
    assert convertPercentToFloat(150) == 1.5