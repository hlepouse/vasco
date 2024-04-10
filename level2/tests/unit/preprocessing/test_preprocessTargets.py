from app.preprocessing import preprocessTargets

def testOneItem():

    targetsList = [
        {
            "year": 2000,
            "month": 4,
            "churnRate": 100,
            "downgradeRate": 50,
            "upgradeRate": 25
        }
    ]

    assert preprocessTargets(targetsList) == { (2000,4) : {
            "year": 2000,
            "month": 4,
            "churnRate": 1,
            "downgradeRate": 0.5,
            "upgradeRate": 0.25
        } }
    
def testValidTwoItemsWithRates():

    targetsList = [
        {
            "year": 2000,
            "month": 4,
            "churnRate": 100,
            "downgradeRate": 50,
            "upgradeRate": 25
        },
        {
            "year": 2000,
            "month": 5,
            "churnRate": 50,
            "downgradeRate": 50,
            "upgradeRate": 25
        }
    ]

    assert preprocessTargets(targetsList) == {
            (2000,4) : {
                "year": 2000,
                "month": 4,
                "churnRate": 1,
                "downgradeRate": 0.5,
                "upgradeRate": 0.25
            },
            (2000,5) : {
                "year": 2000,
                "month": 5,
                "churnRate": 0.5,
                "downgradeRate": 0.5,
                "upgradeRate": 0.25
            },
        }
    
def testDuplicates():

    targetsList = [
        {
            "year": 2000,
            "month": 4,
            "churnRate": 100,
            "downgradeRate": 50,
            "upgradeRate": 25
        },
        {
            "year": 2000,
            "month": 4,
            "churnRate": 100,
            "downgradeRate": 50,
            "upgradeRate": 25
        }
    ]

    assert preprocessTargets(targetsList) == { (2000,4) : {
            "year": 2000,
            "month": 4,
            "churnRate": 1,
            "downgradeRate": 0.5,
            "upgradeRate": 0.25
        } }