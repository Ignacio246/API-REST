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

app = FastAPI()

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


@app.get("/clientes/{id_clientes}", response_model=Cliente)
async def clientes():
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM clientes')
        response = cursor.fetchone()
        return response


@app.post("/cliente/", response_model=Respuesta)
async def post_cliente(cliente=Cliente):
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("insert into clientes(nombre,email) values (?,?)", ("ignacio","nacho@email.com"))
        cursor.execute("SELECT *FROM clientes")
        connection.commit()
        connection.close()
        clientes = cursor.fetchall()
        return clientes


@app.put("/clientes/", response_model=Respuesta)
async def put_cliente(cliente=Cliente):
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("""UPDATE clientes set nombre = ? where id_clientes = ?""",("ignaciocandia",4))
        cursor.execute("SELECT *FROM clientes")
        connection.commit()
        connection.close()
        clientes = cursor.fetchall()
        return clientes

@app.delete("/clientes/", response_model=Respuesta)
async def delete_cliente(cliente=Cliente):
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("DELETE FROM clientes WHERE id_clientes = 4")
        connection.commit()
        connection.close()
        clientes = cursor.fetchall()
        return clientes