from app.computing import computePreviousRecurringRevenue
import os
from app.utils.YearMonth import YearMonth

def test():

    targets = {
        YearMonth(2000,1): {
            "recurringRevenue": 10
        },
        YearMonth(2000,2): {
            "recurringRevenue": 20
        }
    }

    assert computePreviousRecurringRevenue(targets, YearMonth(2000, 2)) == 10
    assert computePreviousRecurringRevenue(targets, YearMonth(2000, 1)) == float(os.getenv("DEFAULT_PREVIOUS_RECURRING_REVENUE"))
