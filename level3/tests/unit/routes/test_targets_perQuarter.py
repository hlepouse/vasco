from app.routes.targets_perQuarter import validate, process
import json
from app.utils.YearMonth import YearMonth

def testProcess():

    targets = {
        YearMonth(2022,1): {
            "recurringRevenue": 100000,
            "churnRate": 0.01,
            "downgradeRate": 0.01,
            "upgradeRate": 0.01,
        },
        YearMonth(2022,2): {
            "recurringRevenue": 100000,
            "churnRate": 0.01,
            "downgradeRate": 0.01,
            "upgradeRate": 0.01,
        },
        YearMonth(2022,3): {
            "recurringRevenue": 100000,
            "churnRate": 0.01,
            "downgradeRate": 0.01,
            "upgradeRate": 0.01,
        }
    }

    assert process(targets, {"year": 2022, "quarter": 1}) == {
            "quarter": 1,
            "year": 2022,
            "recurringRevenue": 100000,
            "churnRate": 0.03,
            "downgradeRate": 0.03,
            "upgradeRate": 0.03,
            "acquisitionTarget": 0,
            "expansionTarget": 3000
        }

    assert process(targets, {"year": 2021, "quarter": 2}) == {}