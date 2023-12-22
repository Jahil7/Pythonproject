import product.product as p
import Login.Loginuser as l
def User():
    print("1 for Login")
    ch = int(input("Enter 1 for login: " ))
    if (ch== 1):
        if(l.Login()):
            print("User login Successful")
            p.product()
        else: 
           print("User Not login")
User()