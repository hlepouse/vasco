from app.Computer import Computer
import os
from app.utils.YearMonth import YearMonth

def test():

    targetsList = [
        {
            "year": 2000,
            "month": 1,
            "recurringRevenue": 10
        },
        {
            "year": 2000,
            "month": 2,
            "recurringRevenue": 20
        }
    ]

    computer = Computer(targetsList, [], 100000)

    assert computer.computePreviousRecurringRevenue(YearMonth(2000, 2)) == 10
    assert computer.computePreviousRecurringRevenue(YearMonth(2000, 1)) == 100000
