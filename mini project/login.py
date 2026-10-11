#simple login page logic 
user = {
     "adarsh": "1234",
     "admin": "adminpass"
}

def login(username, password):
     if username in user:
          if user[username] == password:
               return "Login Successful"
          else:
               return "wrong password"
     else:
          return "user not found"
