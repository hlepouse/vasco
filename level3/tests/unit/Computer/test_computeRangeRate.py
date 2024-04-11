from app.Computer import Computer
from app.utils.YearMonth import YearMonth
from app.utils.YearMonthRange import YearMonthRange

def test():

    targetsList = [
        {
            "year": 2000,
            "month": 1,
            "recurringRevenue": 10,
            "churnRate": 0.01
        },
        {
            "year": 2000,
            "month": 2,
            "recurringRevenue": 20,
            "churnRate": 0.02
        }
    ]

    computer = Computer(targetsList)

    # (10 * 0.01 + 10 * 0.02) / 15
    assert round(computer.computeRangeRate("churnRate", 10, 15, YearMonthRange(YearMonth(2000, 1), YearMonth(2000, 2))), 3) == 0.02