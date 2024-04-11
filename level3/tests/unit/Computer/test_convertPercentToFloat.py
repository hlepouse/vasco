from app.Computer import Computer

def testValidConversion():

    assert Computer.convertPercentToFloat(-50) == -0.5
    assert Computer.convertPercentToFloat(0) == 0
    assert Computer.convertPercentToFloat(50) == 0.5
    assert Computer.convertPercentToFloat(100) == 1
    assert Computer.convertPercentToFloat(150) == 1.5