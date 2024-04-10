from app.routes.targets_perMonth import validate, process
import json

def testProcess():

    targets = {
        (2022,6): {
            "recurringRevenue": 145000.0,
            "churnRate": 0.01,
            "downgradeRate": 0.03,
            "upgradeRate": 0.02,
        }
    }

    assert process(targets, {"year": 2022, "month": 6}) == {
            "month": 6,
            "year": 2022,
            "recurringRevenue": 145000.0,
            "churnRate": 0.01,
            "downgradeRate": 0.03,
            "upgradeRate": 0.02,
            "acquisitionTarget": 45000,
            "expansionTarget": 2000
        }

    assert process(targets, {"year": 2021, "month": 6}) == {}