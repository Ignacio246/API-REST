from fastapi import FastAPI
from fastapi import Depends, Fastapi, HTTPException, status, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

import pyrebase

app = Fastapi()



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

securityBasic = HTTPBasic()
securityBearer = HTTPBearer()

@app.get("/", response_model=Respuesta)
async def index():
    return {"message": "API-REST"}


@app.get(
    "/users/token",
    status_code = status.HTTP_202_ACCEPTED,
    summary="Get atoken for user",
    description="Get atoken for user",
    tags=["auth"]
)
async def get_token(credentials:HTTPBasicCredentials = Depends(securityBasic)):
    try:
        email = credentials.username
        password = credentials.password
        auth = firebase.auth()
        user = auth.sign_in_with_email_and_password(email, password)
        response ={
            "token": user['idToken']
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
async def get_user(credentials:HTTPBasicCredentials = Depends(securityBearer)):
    try:
        auth = firebase.auth()
        user = auth.get_account_info(credentials.credentials)
        uid =user['users'][0]['localId']
        db = firebase.database()
        user_data = db.child("users").child(uid).get().val()
        response = {
            "user_data": user_data
        }
        return response
    except Exception as error:
         print(f"ERROR: {error}")
    raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED)