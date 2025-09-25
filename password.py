#passowrd manager!
master_pwd = input("Enter a MASTER PASSWORD! \n")# user input

def view():
    with open ('password.txt','r') as f:
        f.read('password.txt')

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open ('password.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)?")
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:

        print("invalid mode.")
