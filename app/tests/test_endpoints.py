from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_banks():
    response = client.get("/banks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_branch_by_ifsc():
    response = client.get("/branches/SOME_IFSC_CODE")
    if response.status_code == 200:
        assert "branch" in response.json()
        assert "ifsc" in response.json()
        assert "bank" in response.json()
    else:
        assert response.status_code == 404
