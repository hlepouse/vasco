from app.computing import computeRecurringRevenue

def test():

    targets = {
        (2000,1): {
            "recurringRevenue": 10
        },
        (2000,2): {
            "recurringRevenue": 20
        }
    }

    assert computeRecurringRevenue(targets, 2000, 1, 2000, 2) == 20
