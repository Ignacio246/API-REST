from fastapi import FastAPI
import hashlib  # importa la libreria hashlib
import sqlite3
import os
from typing import List

import sqlite3 
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
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
        cursor.execute("INSERT INTO clientes (nombre,email VALUES (4,'ignacio','nacho@email.com')",
        (Cliente.id_clientes,Cliente.nombre,Cliente.email))
        connection.commit()
        connection.close()
        return {"message": "Cliente guardado"}

@app.put("/clientes/", response_model=Respuesta)
async def put_cliente(cliente=Cliente):
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("UPDATE clientes SET nombre = ignacio, email = nachoci12@email.com WHERE id_clientes = 4')",
        (cliente.id_clientes,cliente.nombre,cliente.email))
        connection.commit()
        connection.close()
        return {"message": "Cliente actualizado"}

@app.delete("/clientes/{id_clientes}", response_model=Respuesta)
async def delete_cliente(cliente=Cliente):
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("DELETE FROM clientes WHERE ID = 4",(Cliente.id_clientes))
        connection.commit()
        connection.close()
        return {"message": "Cliente eliminado"}
"""

@app.post("/clientes/"
    )
def post_cliente(nombre: str, email:str):
    return f"Cliente {nombre} {email} guardado"

@app.put("/clientes/")
def put_cliente(nombre: str, email:str):
    return f"Cliente {nombre} {email} actualizado"

@app.delete("/clientes/{id_clientes}")
def delete_clientes(id_clientes: int):
    return f"Cliente {id_clientes} eliminado"
