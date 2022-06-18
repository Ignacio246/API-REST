from fastapi import FastAPI

import sqlite3 
from typing import List
from pydantic import BaseModel

class Respuesta(BaseModel):
    message: str

class Cliente(BaseModel):
    id_clientes: int
    nombre: str
    email: str

class Cliente(BaseModel):
    id_clientes: int
    nombre: str
    email: str

app = FastAPI()


@app.get("/", response_model=Respuesta)
async def index():
    return {"message": "API-REST"}



@app.get("/clientes/", response_model=List[Cliente])
async def clientes():
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM clientes')
        response = cursor.fetchall()
        return response


"""
@app.get("/clientes/", response_model=List[Cliente])
async def clientes(offset:int=0,limit:int=10):
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM clientes OFFSET & LIMIT ?',(offset,limit))
        response = cursor.fetchall()
        return response
"""

@app.get("/clientes/{id_clientes}", response_model=Cliente)
async def clientes():
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM clientes')
        response = cursor.fetchone()
        return response
"""
@app.post("/clientes/", response_model=Respuesta)
async def post_cliente(cliente=Cliente):
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("INSERT INTO clientes (nombre,email VALUES ('ignacio','nacho@email.com')")
        connection.commit()
        connection.close()
"""

@app.post("/clientes/")
def post_cliente(nombre: str, email:str):
    return f"Cliente {nombre} {email} guardado"

@app.put("/clientes/")
def put_cliente(nombre: str, email:str):
    return f"Cliente {nombre} {email} actualizado"

@app.delete("/clientes/{id_clientes}")
def delete_clientes(id_clientes: int):
    return f"Cliente {id_clientes} eliminado"
