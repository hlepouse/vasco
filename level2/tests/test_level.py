import json

def testMonth(client):

    response = client.get('/trpc/targets.perMonth', query_string = { "input": json.dumps({
        "month": 6,
        "year": 2022
    })})
    assert response.json == {
            "month": 6,
            "year": 2022,
            "recurringRevenue": 145000.0,
            "churnRate": 0.01,
            "downgradeRate": 0.03,
            "upgradeRate": 0.02,
        }
    
def testQuarter(client):

    response = client.get('/trpc/targets.perQuarter', query_string = { "input": json.dumps({
        "quarter": 2,
        "year": 2022
    })})
    assert response.json == {
            "quarter": 2,
            "year": 2022,
            "recurringRevenue": 145000.0,
            "churnRate": 0.028,
            "downgradeRate": 0.085,
            "upgradeRate": 0.056,
        }