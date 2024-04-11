from app.computing import computeRangeMetrics
from app.utils.YearMonth import YearMonth
from app.utils.YearMonthRange import YearMonthRange

def test():

    targets = {
        YearMonth(2000,1): {
            "recurringRevenue": 10,
            "churnRate": 0.01,
            "downgradeRate": 0.01,
            "upgradeRate": 0.01
        },
        YearMonth(2000,2): {
            "recurringRevenue": 20,
            "churnRate": 0.02,
            "downgradeRate": 0.02,
            "upgradeRate": 0.02
        }
    }

    # (100000 * 0.01 + 10 * 0.02) / 15 = 66.68
    assert computeRangeMetrics(targets, YearMonthRange(YearMonth(2000, 1), YearMonth(2000, 2))) == {
        "recurringRevenue": 20,
        "churnRate": 66.68,
        "downgradeRate": 66.68,
        "upgradeRate": 66.68,
        "acquisitionTarget": -99980,
        "expansionTarget": 1000.2
    }

def testDivisionByZero():

    targets = {
        YearMonth(2000,1): {
            "recurringRevenue": 0,
            "churnRate": 0.01,
            "downgradeRate": 0.01,
            "upgradeRate": 0.01
        },
        YearMonth(2000,2): {
            "recurringRevenue": 0,
            "churnRate": 0.02,
            "downgradeRate": 0.02,
            "upgradeRate": 0.02
        }
    }

    assert computeRangeMetrics(targets, YearMonthRange(YearMonth(2000, 1), YearMonth(2000, 2))) == {
        "recurringRevenue": 0,
        "churnRate": None,
        "downgradeRate": None,
        "upgradeRate": None,
        "acquisitionTarget": -100000,
        "expansionTarget": 1000

    }