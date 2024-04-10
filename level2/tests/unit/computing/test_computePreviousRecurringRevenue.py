from app.computing import computePreviousRecurringRevenue
import os

def test():

    targets = {
        (2000,1): {
            "recurringRevenue": 10
        },
        (2000,2): {
            "recurringRevenue": 20
        }
    }

    assert computePreviousRecurringRevenue(targets, 2000, 2) == 10
    assert computePreviousRecurringRevenue(targets, 2000, 1) == float(os.getenv("DEFAULT_PREVIOUS_RECURRING_REVENUE"))
