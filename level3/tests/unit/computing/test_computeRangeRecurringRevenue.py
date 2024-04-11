from app.computing import computeRangeRecurringRevenue
from app.utils.YearMonth import YearMonth
from app.utils.YearMonthRange import YearMonthRange

def test():

    targets = {
        YearMonth(2000,1): {
            "recurringRevenue": 10
        },
        YearMonth(2000,2): {
            "recurringRevenue": 20
        }
    }

    assert computeRangeRecurringRevenue(targets, YearMonthRange(YearMonth(2000, 1), YearMonth(2000, 2))) == 20
