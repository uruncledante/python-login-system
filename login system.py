# enter name and id
name = input("Enter your name: ")
id = input("Enter your ID: ")

#ask user to create a password
password = input ("Create a password: ")

#now ask user to login with name and password
while True:
    login_name = input("enter your name: ")
    login_password = input("Enter your password: ")
    if login_name == name and login_password == password:
        print("Hello, "+name+"! your ID is: "+id)
        break
    else:
        print("username or password is incorrect, please try again.")