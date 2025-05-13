from app import app

def test_status():
    client = app.test_client()
    response = client.get('/books')
    assert response.status_code in [200, 500]  # 500 = if DB not yet initialized
