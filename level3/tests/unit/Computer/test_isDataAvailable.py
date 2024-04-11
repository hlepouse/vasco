from app.Computer import Computer
from app.utils.YearMonth import YearMonth
from app.utils.YearMonthRange import YearMonthRange

def test():

    targetsList = [
        {
            "year": 2000,
            "month": 1,
        }
    ]

    computer = Computer(targetsList)

    assert computer.isDataAvailable(YearMonthRange(YearMonth(2000, 1), YearMonth(2000, 1)))
    assert not computer.isDataAvailable(YearMonthRange(YearMonth(2000, 1), YearMonth(2000, 2)))
