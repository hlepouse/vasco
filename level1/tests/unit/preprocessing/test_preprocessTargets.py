from app.preprocessing import preprocessTargets

def testOneItem():

    targetsList = [
        {
            "year": 2000,
            "month": 4
        }
    ]

    assert preprocessTargets(targetsList) == { (2000,4) : {
            "year": 2000,
            "month": 4
        } }
    
def testValidTwoItemsWithRates():

    targetsList = [
        {
            "year": 2000,
            "month": 4,
            "churnRate": 100
        },
        {
            "year": 2000,
            "month": 5,
            "churnRate": 50
        }
    ]

    assert preprocessTargets(targetsList) == {
            (2000,4) : {
                "year": 2000,
                "month": 4,
                "churnRate": 1
            },
            (2000,5) : {
                "year": 2000,
                "month": 5,
                "churnRate": 0.5
            },
        }
    
def testDuplicates():

    targetsList = [
        {
            "year": 2000,
            "month": 4
        },
        {
            "year": 2000,
            "month": 4
        }
    ]

    assert preprocessTargets(targetsList) == { (2000,4) : {
            "year": 2000,
            "month": 4
        } }