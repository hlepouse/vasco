from app.computing import computeAverageRecurringRevenue

def test():

    targets = {
        (2000,1): {
            "recurringRevenue": 10
        },
        (2000,2): {
            "recurringRevenue": 20
        }
    }

    assert computeAverageRecurringRevenue(targets, 2000, 1, 2000, 2) == 15
