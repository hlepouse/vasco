from app.computing import computeRangeAverageRecurringRevenue

def test():

    targets = {
        (2000,1): {
            "recurringRevenue": 10
        },
        (2000,2): {
            "recurringRevenue": 20
        }
    }

    assert computeRangeAverageRecurringRevenue(targets, 2, 2000, 1, 2000, 2) == 15
