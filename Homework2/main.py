users = {}



def add_user(username, password):
    if username in users:
        return "User already exists."
    
    users[username] = password
    return "User added successfully."
def print_users():
    for username in users:
        print(f"User: {username}, Password: {users[username]}")
def delete_user(username):
    if username not in users:
        return "User does not exist."
    del users[username]
    return "User deleted successfully."

def change_password(username, new_password):
    if username not in users:
        return "User does not exist."
    if(new_password.isalpha() or len(new_password) < 6):
        return "New password is too weak."
    users[username] = new_password
    return "Password changed successfully."


def check_password():
    for username, password in users.items():
        if(password.isalpha() or len(password) < 6):
            print(f"User '{username}' has a weak password.")


def get_password(username):
    return f"pass {username} == {users[username]}"



print("------------------All Users-----------------------")

add_user("Dmytro", "Dmytr0_123")
add_user("Olena", "Olena#_456")
add_user("WeakUser1", "pass")
add_user("WeakUser2", "passwordonly")
add_user("Dmytro", "AnotherP@ss")
print_users()
change_password("Dmytro", "SuperP@ssw0rd")
change_password("Olena", "short")
print("---------------------Change pass--------------------")
print_users()

print("---------------------Check pass--------------------")
check_password()

print("---------------------Delete user --------------------")

delete_user("WeakUser1")
print_users()
