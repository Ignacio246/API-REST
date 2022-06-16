from fastapi.testclient import TestClient 
from code.main import app

clientes = TestClient(app)

##def test_index():
##    response = clientes.get("/")
##    assert response.status_code == 200
##    assert response.json() == {"message": "Hello World"}

def test_index():
    response = clientes.get("/")
    data = {"message":"Hola mundo"}
    assert response.status_code == 200
    assert response.json() == data

def test_clientes():
    response = clientes.get("/clientes/")
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

        }
    ]
    assert response.status_code == 200
    assert response.json() == data