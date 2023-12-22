import DataM.Data as dd

def Login():

    username = input("enter username: ")
    password =int(input("enter userpassword: "))
    # print(username)
    # print(password)
    return dd.Datauser1(username,password)