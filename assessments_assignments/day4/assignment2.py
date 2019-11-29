credentials = [
    {"username": "Sachin", "password": "icc"},
    {"username": "rahul", "password": "bcc"}
]
try:
    username = input("Enter the username")
    passsword = input("Enter the password")
    for item in credentials:
        if(item["username"] == username and item["password"] == passsword):
            print("Hi {0}, Welcome!".format(username))
            break
    else:
        raise Exception("Username/Password does not exist")

except Exception as e:
    print(e)