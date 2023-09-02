def authenticate(username, password, auth_code, login_username, login_password, provided_auth_code):
    users = []    
    registered_user = {"username": username, "password": password, "auth_code": auth_code}
    users.append(registered_user)
    for user in users:
        if user['username'] == login_username:
            if user['username'] == login_username and user['password'] == login_password:
                if user['auth_code'] == provided_auth_code:
                    return f"Access granted for {login_username}."
                else: return f"Incorrect authentication code for {login_username}. Access denied."
        else:
            return f"User {login_username} not found. Access denied."
    return f"Incorrect password for {login_username}. Access denied."
    

def main():
    username = input()
    password = input()
    
    auth_code = input()
    
    login_username = input()
    login_password = input()
    
    provided_auth_code = input()
    
    result = authenticate(username, password, auth_code, login_username, login_password, provided_auth_code)  
    print(result)

if __name__ == "__main__":
    main()