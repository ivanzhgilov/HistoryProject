from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_health_endpoint():
  response = client.get("/api/health")
  assert response.status_code == 200
  assert response.json() == {"ok": True}


def test_epochs_endpoint():
  response = client.get("/api/epochs")
  assert response.status_code == 200
  body = response.json()
  assert "epochs" in body
  assert isinstance(body["epochs"], list)
  assert len(body["epochs"]) > 0


def test_epoch_not_found_shape():
  response = client.get("/api/epochs/does-not-exist")
  assert response.status_code == 404
  body = response.json()
  assert body["error"] == "Not Found"
  assert body["resource"] == "epoch"
