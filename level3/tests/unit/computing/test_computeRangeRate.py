from app.computing import computeRangeRate
from app.utils.YearMonth import YearMonth
from app.utils.YearMonthRange import YearMonthRange

def test():

    targets = {
        YearMonth(2000,1): {
            "recurringRevenue": 10,
            "churnRate": 0.01
        },
        YearMonth(2000,2): {
            "recurringRevenue": 20,
            "churnRate": 0.02
        }
    }

    # (10 * 0.01 + 10 * 0.02) / 15
    assert round(computeRangeRate(targets, "churnRate", 10, 15, YearMonthRange(YearMonth(2000, 1), YearMonth(2000, 2))), 3) == 0.02