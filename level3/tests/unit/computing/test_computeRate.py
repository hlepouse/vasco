from app.computing import computeRate

def test():

    targets = {
        (2000,1): {
            "recurringRevenue": 10,
            "churnRate": 0.01
        },
        (2000,2): {
            "recurringRevenue": 20,
            "churnRate": 0.02
        }
    }

    # (100000 * 0.01 + 10 * 0.02) / 15
    assert computeRate(targets, "churnRate", 15, 2000, 1, 2000, 2) == 66.68