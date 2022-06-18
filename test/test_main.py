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

def test_post_cliente():
    payload = {"id_cliente":4,"nombre":"ignacio","email":"nacho@email.com"}
    response = clientes.post("/clientes/", json=payload)
    data = {"message":"Cliente guardado"}
    assert response.status_code == 200
    assert response.json() == data

def test_put_cliente():
    payload = {
        "id_clientes": 4,
        "nombre":"ignacio",
        "email":"nacho12@email.com",
    }
    response = clientes.put("/clientes/", json=payload)
    data = {"message":"Cliente actualizado"}
    assert response.status_code == 200
    assert response.json() == data

def test_delete_cliente():
    response = clientes.delete("/clientes/4")
    data = {"message":"Cliente eliminado"}
    assert response.status_code == 200
    assert response.json() == data


    