from app.preprocessing import preprocessTargets
from app.utils.YearMonth import YearMonth

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

    assert preprocessTargets(targetsList) == { YearMonth(2000,4) : {
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
            YearMonth(2000,4) : {
                "churnRate": 1,
                "downgradeRate": 0.5,
                "upgradeRate": 0.25
            },
            YearMonth(2000,5) : {
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

    assert preprocessTargets(targetsList) == { YearMonth(2000,4) : {
            "churnRate": 1,
            "downgradeRate": 0.5,
            "upgradeRate": 0.25
        } }