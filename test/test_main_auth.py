from fastapi.testclient import TestClient 
from code.main import app

clientes = TestClient(app)

def test_post_cliente_4():
    auth = HTTPBasicAuth(username="user", password="user")
    payload = {"id_clientes":7,"nombre":"ignacio","email":"nacho@email.com"}
    response = clientes.post(
        "/clientes/",
        json=payload,
        auth=auth,
        headers={"content-type": "application/json"}
    )
    data = {"mensaje": "El cliente se agrego"}
    assert response.status_code == 202
    assert response.json() == data