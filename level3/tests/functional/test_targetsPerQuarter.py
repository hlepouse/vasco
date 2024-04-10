import json

def testValidInput(client):

    response = client.get('/trpc/targets.perQuarter', query_string = { "input": json.dumps({
        "quarter": 4,
        "year": 2022
    })})
    assert response.status_code == 200
    
def testInvalidInputs(client):

    response = client.get('/trpc/targets.perQuarter')
    assert response.status_code == 400

    response = client.get('/trpc/targets.perQuarter', query_string = { "a": "qffsd" })
    assert response.status_code == 400
