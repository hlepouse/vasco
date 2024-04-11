from app.Computer import Computer
from app.utils.YearMonth import YearMonth

def test():

    targetsList = [
        {
            "year": 2000,
            "month": 1,
            "recurringRevenue": 10
        }
    ]

    computer = Computer(targetsList, [], 100000)

    assert computer.computeAcquisitionTarget(YearMonth(2000, 1)) == -99990
