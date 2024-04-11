from app.Computer import Computer
from app.utils.YearMonth import YearMonth

def test():

    targetsList = [
        {
            "year": 2000,
            "month": 1,
            "recurringRevenue": 10,
            "churnRate": 1,
            "downgradeRate": 1,
            "upgradeRate": 1
        }
    ]

    computer = Computer(targetsList, [], 100000)

    assert computer.computeNetRetentionRate(YearMonth(2000, 1)) == 0
