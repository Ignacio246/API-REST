import hashlib  # importa la libreria hashlib
import sqlite3
import os
from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

app = FastAPI()

DATABASE_URL = os.path.join("sql/clientes.sqlite")

security = HTTPBasic()




class Usuarios(BaseModel):
    username: str
    level: int


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

@app.get(
    "/usuarios/",
    response_model=List[Usuarios],
    status_code=status.HTTP_202_ACCEPTED,
    summary="Regresa una lista de usuarios",
    description="Regresa una lista de usuarios",
)
async def get_usuarios(level: int = Depends(get_current_level)):
    if level == 0:  # Administrador
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