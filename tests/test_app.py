from app import app

def test_status():
    client = app.test_client()
    res = client.get('/status')
    assert res.status_code == 200
    data = res.get_json()
    assert 'name' in data and 'env' in data
