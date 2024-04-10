from app.computing import computeMetrics

def test():

    targets = {
        (2000,1): {
            "recurringRevenue": 10,
            "churnRate": 0.01,
            "downgradeRate": 0.01,
            "upgradeRate": 0.01
        },
        (2000,2): {
            "recurringRevenue": 20,
            "churnRate": 0.02,
            "downgradeRate": 0.02,
            "upgradeRate": 0.02
        }
    }

    # (100000 * 0.01 + 10 * 0.02) / 15
    assert computeMetrics(targets, 2000, 1, 2000, 2) == {
        "recurringRevenue": 20,
        "churnRate": 66.68,
        "downgradeRate": 66.68,
        "upgradeRate": 66.68
    }

def testDivisionByZero():

    targets = {
        (2000,1): {
            "recurringRevenue": 0,
            "churnRate": 0.01,
            "downgradeRate": 0.01,
            "upgradeRate": 0.01
        },
        (2000,2): {
            "recurringRevenue": 0,
            "churnRate": 0.02,
            "downgradeRate": 0.02,
            "upgradeRate": 0.02
        }
    }

    assert computeMetrics(targets, 2000, 1, 2000, 2) == {
        "recurringRevenue": 0,
        "churnRate": None,
        "downgradeRate": None,
        "upgradeRate": None
    }