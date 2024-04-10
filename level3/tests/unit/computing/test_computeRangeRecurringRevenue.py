from app.computing import computeRangeRecurringRevenue

def test():

    targets = {
        (2000,1): {
            "recurringRevenue": 10
        },
        (2000,2): {
            "recurringRevenue": 20
        }
    }

    assert computeRangeRecurringRevenue(targets, 2000, 1, 2000, 2) == 20
