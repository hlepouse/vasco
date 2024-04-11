from app.Computer import Computer
from app.utils.YearMonth import YearMonth
from app.utils.YearMonthRange import YearMonthRange

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
    
    computer = Computer(targetsList)

    assert computer.computeRangeRecurringRevenue(YearMonthRange(YearMonth(2000, 1), YearMonth(2000, 2))) == 20
