from app.Computer import Computer
from app.utils.YearMonth import YearMonth
from app.utils.YearMonthRange import YearMonthRange

def test():

    targetsList = [
        {
            "year": 2000,
            "month": 1,
            "recurringRevenue": 10,
            "churnRate": 1,
            "downgradeRate": 1,
            "upgradeRate": 1
        },
        {
            "year": 2000,
            "month": 2,
            "recurringRevenue": 20,
            "churnRate": 2,
            "downgradeRate": 2,
            "upgradeRate": 2
        }
    ]

    computer = Computer(targetsList, ["churnRate","downgradeRate","upgradeRate"], 100000)

    # (100000 * 0.01 + 10 * 0.02) / 15 = 66.68
    assert computer.computeRangeMetrics(YearMonthRange(YearMonth(2000, 1), YearMonth(2000, 2))) == {
        "recurringRevenue": 20,
        "churnRate": 66.68,
        "downgradeRate": 66.68,
        "upgradeRate": 66.68,
        "acquisitionTarget": -99980,
        "expansionTarget": 1000.2
    }

def testDivisionByZero():

    targetsList = [
        {
            "year": 2000,
            "month": 1,
            "recurringRevenue": 0,
            "churnRate": 1,
            "downgradeRate": 1,
            "upgradeRate": 1
        },
        {
            "year": 2000,
            "month": 2,
            "recurringRevenue": 0,
            "churnRate": 2,
            "downgradeRate": 2,
            "upgradeRate": 2
        }
    ]

    computer = Computer(targetsList, ["churnRate","downgradeRate","upgradeRate"], 100000)

    assert computer.computeRangeMetrics(YearMonthRange(YearMonth(2000, 1), YearMonth(2000, 2))) == {
        "recurringRevenue": 0,
        "churnRate": None,
        "downgradeRate": None,
        "upgradeRate": None,
        "acquisitionTarget": -100000,
        "expansionTarget": 1000

    }