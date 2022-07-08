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
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.responses import FileResponse

app = FastAPI()

origins = [
    "https://8080-ignacio246-apirest-gznbfv3i6l3.ws-us53.gitpod.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Respuesta(BaseModel):
    message: str

class Cliente(BaseModel):
    id_clientes: int
    nombre: str
    email: str

class ClienteIN(BaseModel):
    nombre: str
    email: str

class ClienteUP(BaseModel):
    id_clientes: int
    nombre: str
    email: str

class ClienteDE(BaseModel):
    id_clientes: int
    
    


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
async def clientes(id_clientes : int):
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT id_clientes,nombre,email FROM clientes where id_clientes = ?",(id_clientes,))
        response = cursor.fetchone()
        if response is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cliente no encontrado",
                headers={"www-Authenticate": "Basic"},
        )
        return response

@app.post("/clientes/", response_model=Respuesta)
async def post_clientes(cliente: ClienteIN):
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("INSERT INTO clientes (nombre,email) VALUES (?,?)",
        (cliente.nombre, cliente.email),
        )
        connection.commit()
        return {"message": "Cliente creado"}


@app.put("/clientes/{id_clientes}", response_model=Respuesta)
async def put_clientes(cliente:ClienteUP):
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("UPDATE clientes set nombre = ?, email = ? where id_clientes = ?""",
        (cliente.nombre, cliente.email, cliente.id_clientes),
        )
        connection.commit()
        cursor.execute("SELECT *FROM clientes")
        return {"message": "Cliente Actualizado"}

@app.delete("/clientes/{id_clientes}", response_model=Respuesta)
async def delete_clientes(cliente:Cliente):
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("DELETE FROM clientes where id_clientes = ?""",
        (cliente.id_clientes,)
        )
        connection.commit()
        cursor.execute("SELECT *FROM clientes")
        return {"message": "Cliente Eliminado"}






"""
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
        cursor.execute("UPDATE clientes set nombre = ? where id_clientes = ?",("ignaciocandia",4))
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
"""

"""
@app.get("/", response_class=FileResponse)
async def redirect_typer():
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM clientes')
        response = cursor.fetchall()
    return FileResponse("/workspace/API-REST/frontend/get_clientes.html")
"""