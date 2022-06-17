from fastapi.testclient import TestClient 
from code.main import app

clientes = TestClient(app)

"""
def test_index():
    response = clientes.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
"""
"""
def test_index():
    response = clientes.get("/")
    data = {"message": "API-REST"}
    assert response.status_code == 200
    assert response.json() == data
"""


def test_clientes():
    response = clientes.get("/clientes/?offset=0&limit=3")
    data = [
        {
            "id_clientes": 1,
            "nombre": "Rodrigo",
            "email": "rodri@email.com",

        },
        {
            "id_clientes": 2,
            "nombre": "David",
            "email": "david@email.com",

        },
         {
            "id_clientes": 3,
            "nombre": "Karen",
            "email": "karen@email.com",

        }
    ]
    assert response.status_code == 200
    assert response.json() == data