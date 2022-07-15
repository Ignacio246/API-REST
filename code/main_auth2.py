import pyrebase

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

db=firebase.database()
auth=firebase.auth()
storage=firebase.storage()
"""
#Login
email=input('Enter your email')
password=input('Enter your password')
try:
    auth.sign_in_with_email_and_password(email,password)
    print('Succesfully signed in!')
except:
    print("Invalidad user or password. Try again.")
"""
#Signup
email=input('Enter your email')
password=input('Enter your password')
confirmpass=input("Confirm your password")
if password==confirmpass:
    auth.create_user_with_email_and_password(email, password)

##Minuto 16:00 