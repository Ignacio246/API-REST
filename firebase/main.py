import hashlib
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Depends, FastAPI, HTTPException, status, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware

import pyrebase

app = FastAPI()


origins = [
    "https://1234-ignacio246-apirest-gznbfv3i6l3.ws-us54.gitpod.io",
    "https://8080-ignacio246-apirest-gznbfv3i6l3.ws-us54.gitpod.io",
    "https://8000-ignacio246-apirest-gznbfv3i6l3.ws-us54.gitpod.io",
    "https://8000-ignacio246-apirest-gznbfv3i6l3.ws-us59.gitpod.io",
    "https://8080-ignacio246-apirest-gznbfv3i6l3.ws-us59.gitpod.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


firebaseConfig={
  'apiKey': "AIzaSyBXo2gTqSoNvIKkdjQZNvuUcUyE5ITaEuo",
  'authDomain': "authentication-88a73.firebaseapp.com",
  'databaseURL': 'https://authentication-88a73-default-rtdb.firebaseio.com',
  'projectId': "authentication-88a73",
  'storageBucket': "authentication-88a73.appspot.com",
  'messagingSenderId': "57781738429",
  'appId': "1:57781738429:web:d56c15c63b86614e0650d4",
  'measurementId': "G-81XCZ3TBHD"
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

securityBasic = HTTPBasic()
securityBearer = HTTPBearer()

class Respuesta(BaseModel):
    message: str

class Usuario(BaseModel):
    email: str
    password: str

@app.get("/")
async def index():
    return {"message": "API-REST"}


@app.get(
    "/users/token/",
    status_code = status.HTTP_202_ACCEPTED,
    summary="Get a token for user",
    description="Get a token for user",
    tags=["auth"]
)
async def get_token(credentials:HTTPBasicCredentials = Depends(securityBasic)):
    try:
        email = credentials.username
        password = credentials.password
        auth = firebase.auth()
        user = auth.sign_in_with_email_and_password(email,password)
        response ={
            "token": user['idToken'],
            "uid": user['localId']
        }
        return response
    except Exception as error:
        print(f"ERROR: {error}")
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)

@app.get(
    "/users/",
    status_code = status.HTTP_202_ACCEPTED,
    summary="Get a user",
    description="Get a user",
    tags=["auth"]
)
async def get_user(credentials:HTTPAuthorizationCredentials = Depends(securityBearer)):
    try:
        auth = firebase.auth()        
        user = auth.get_account_info(credentials.credentials)
        uid =user['users'][0]['localId']
        db = firebase.database()
        user_data = db.child("users").child(uid).get().val()
        response = {
            "users": user_data
        }
        return response
    except Exception as error:
         print(f"ERROR: {error}")
    raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)

@app.post(
    "/users/",
    response_model=Respuesta,
    status_code = status.HTTP_202_ACCEPTED,
    summary="Create a user",
    description="Create a user",
    tags=["auth"]
)
async def post_user(usuario:Usuario):
    try:
        auth = firebase.auth()
        user = auth.create_user_with_email_and_password(usuario.email, usuario.password)
        userI = auth.get_account_info(user['idToken'])
        uid =userI['users'][0]['localId']
        db = firebase.database()
        db.child("users").child(uid).set({"email":usuario.email, "nivel":1})
        return {
            
            "message":"Usuario agregdo"
        }
        return response
    except Exception as error:
        print(f"ERROR: {error}")
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)

@app.put(
    "/users/token",
    response_model=Respuesta,
    status_code = status.HTTP_202_ACCEPTED,
    summary="Update a user",
    description="Update a user",
    tags=["auth"]
)
async def put_user(usuario:Usuario, credentials:HTTPAuthorizationCredentials = Depends(securityBearer)):
    try:
        
        userI = auth.get_account_info(credentials.credentials)
        uid =userI['users'][0]['localId']
        db = firebase.database()
        user_data = db.child("users").child(uid).update({"email":usuario.email, "nivel":1})
        return {
            
            "message":"Usuario actualizado"
        }
        response = {
            "user_data": user_data
        }
        return response
    except Exception as error:
        print(f"ERROR: {error}")
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)

@app.delete(
    "/users/token",
    response_model=Respuesta,
    status_code = status.HTTP_202_ACCEPTED,
    summary="Delete a user",
    description="Delete a user",
    tags=["auth"]
)
async def delete_user(credentials:HTTPAuthorizationCredentials = Depends(securityBearer)):
    try:
        
        userI = auth.get_account_info(credentials.credentials)
        uid =userI['users'][0]['localId']
        db = firebase.database()
        user_data = db.child("users").child(uid).remove()
        return {
            
            "message":"Usuario eliminado"
        }
        response = {
            "user_data": user_data
        }
        return response
    except Exception as error:
        print(f"ERROR: {error}")
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)



"""
@app.get(
    "/users/token",
    status_code = status.HTTP_202_ACCEPTED,
    summary="Get a user",
    description="Get a user",
    tags=["auth"]
)
async def get_token(usuario:Usuario, credentials:HTTPBasicCredentials = Depends(securityBasic)):
    try:
        email = credentials.username
        password = credentials.password
        auth = firebase.auth()
        user = auth.sign_in_with_email_and_password(usuario.email, usuario.password)
        response ={
            "token": user['idToken'],
            "uid": user['localId']
        }
        return response
    except Exception as error:
        print(f"ERROR: {error}")
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)

"""
#auth
#db.child("users").child(uid).push(user)