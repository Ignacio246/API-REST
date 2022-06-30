import hashlib  # importa la libreria hashlib
import sqlite3
import os
from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = os.path.join("sql/usuarios.sqlite")

security = HTTPBasic()

class Respuesta(BaseModel):
    message: str

class Usuarios(BaseModel):
    username: str
    level: int

class Cliente(BaseModel):
    id_clientes: int
    nombre: str
    email: str
    


def get_current_level(credentials: HTTPBasicCredentials = Depends(security)):
    password_b = hashlib.md5(credentials.password.encode())
    password = password_b.hexdigest()
    with sqlite3.connect(DATABASE_URL) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT level FROM usuarios WHERE username = ? and password = ?",
            (credentials.username, password),
        )
        user = cursor.fetchone()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
    return user[0]
@app.get("/", 
    response_model=Respuesta)
async def index():
        return {"message": "API-REST"}

@app.get(
    "/usuarios/",
    response_model=List[Usuarios],
    status_code=status.HTTP_202_ACCEPTED,
    summary="Regresa una lista de usuarios",
    description="Regresa una lista de usuarios",
)
async def get_usuarios(level: int = Depends(get_current_level)):
    if level == 1:  # Administrador
        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute("SELECT username, level FROM usuarios")
            usuarios = cursor.fetchall()
            return usuarios
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Don't have permission to access this resource",
            headers={"WWW-Authenticate": "Basic"},
        )

@app.post(
    "/clientes/",
    response_model=List[Cliente],
    status_code=status.HTTP_202_ACCEPTED,
    summary="Regresa los clientes ingresados",
    description="Regresa los clientes ingresados",
)
async def post_clientes(level: int = Depends(get_current_level)):
    if level == 1:  # Administrador
        with sqlite3.connect("sql/clientes.sqlite") as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute("insert into clientes(nombre,email) values (?,?)", ("ignacio","nacho@email.com"))
            cursor.execute("SELECT *FROM clientes")
            clientes = cursor.fetchall()
            return clientes
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Don't have permission to access this resource",
            headers={"WWW-Authenticate": "Basic"},
        )

@app.put(
    "/clientes/{id_clientes}",
    response_model=List[Cliente],
    status_code=status.HTTP_202_ACCEPTED,
    summary="Regresa los clientes actualizados",
    description="Regresa los clientes actualizados",
)
async def put_clientes(level: int = Depends(get_current_level)):
    if level == 1:  # Administrador
        with sqlite3.connect("sql/clientes.sqlite") as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute("""UPDATE clientes set nombre = ? where id_clientes = ?""",("ignaciocandia",4))
            cursor.execute("SELECT *FROM clientes")
            clientes = cursor.fetchall()
            return clientes
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Don't have permission to access this resource",
            headers={"WWW-Authenticate": "Basic"},
        )

@app.delete(
    "/clientes/{id_clientes}",
    response_model=List[Cliente],
    status_code=status.HTTP_202_ACCEPTED,
    summary="Regresa los clientes eliminados",
    description="Regresa los clientes eliminados",
)
async def delete_clientes(level: int = Depends(get_current_level)):
    if level == 1:  # Administrador
        with sqlite3.connect("sql/clientes.sqlite") as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM clientes where id_clientes = 4""")
            cursor.execute("""DELETE FROM clientes where id_clientes = 5""")
            cursor.execute("""DELETE FROM clientes where id_clientes = 6""")
            cursor.execute("SELECT *FROM clientes")
            clientes = cursor.fetchall()
            return clientes
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Don't have permission to access this resource",
            headers={"WWW-Authenticate": "Basic"},
        )

@app.get(
    "/clientes/",
    response_model=List[Cliente],
    status_code=status.HTTP_202_ACCEPTED,
    summary="Regresa una lista de clientes",
    description="Regresa una lista de clientes",
)
async def get_clientes(level: int = Depends(get_current_level)):
    if level == 1:  # Administrador
        with sqlite3.connect("sql/clientes.sqlite") as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM clientes")
            clientes = cursor.fetchall()
            return clientes
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Don't have permission to access this resource",
            headers={"WWW-Authenticate": "Basic"},
        )