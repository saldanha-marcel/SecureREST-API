def perform_login(registered_user, username, password):
    users = []
    users.append(registered_user)
    for user in users:
        if user['username'] == username:
            if user['username'] == username and user['password'] == password:
                return f"Access granted for {username}."
        else:
            return f"User {username} not found. Access denied."

    return f"Incorrect password for {username}. Access denied."

def main():
    registered_username = input()
    registered_password = input()
    
    registered_user = {"username": registered_username, "password": registered_password}
    
    login_username_attempt = input()
    login_password_attempt = input()
    result = perform_login(registered_user, login_username_attempt, login_password_attempt)
    
    print(result)

if __name__ == "__main__":
    main()
