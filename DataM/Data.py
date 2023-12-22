datainfo =[
            {
                "user":["user1","user2","user3"],
                "password":[123,456,789]
            },
            {
                "product":{
                    "productname":["product1","product2","product3"],
                    "productrate":[130,100,120],
                    "productqty":[25,30,40]
                           }
            },
            {"Cart":{
                "productname":[],
                "productqut":[],
                "rate":[]
                    }
            }

            ]

def Datauser1(username,password):
    # print("Data",datainfo)
    user =datainfo[0]
    # print(user)
    datauser = user["user"]
    userpass = user["password"]
    # print(datauser)
    # print(userpass)
    if username in datauser:

        pos = datauser.index(username)
        # print(pos)
        if password == userpass[pos]:

        # print("user found")
           return True
    return False    

def productshow():
     # print(datainfo[1]["product"])
    pro_name = datainfo[1]["product"]["productname"]
    pro_rate = datainfo[1]["product"]["productrate"]
    pro_qty = datainfo[1]["product"]["productqty"]
    for i in range(len(pro_name)):
        print(pro_name[i],"\t",end="")
        print(pro_rate[i],"\t",end="")
        print(pro_qty[i],"\t",end="")
        print()

def Addcart():
    print("__________Add Cart_____________")
    cartproductname = datainfo[2]['Cart']['productname']
    cartproductqty = datainfo[2]['Cart']['productqut']
    print(cartproductname)
    print(cartproductqty)
    
    while True:
        ch =int(input("1 for product 2 for break: "))
        if ch ==1:
            pname = input("enter Productname:  ")
            if pname in datainfo[1]['product']['productname']:
                qty = int(input("enter qty: "))
                cartproductname.append(pname)
                cartproductqty.append(qty)
                  
        elif ch==2:
            break
        else:
            print("enter product: ")
    print("__________Show cart____________")
    datacart= datainfo[2]['Cart']
    dataprd= datainfo[1]['product']
    dataprdname = datainfo[1]['product']['productname'] 
    datarate= datainfo[2]['Cart']['rate']


    # print(datacart)
    # print(dataprd)
    # print(dataprdname)
    # print(datarate)

    for i in datacart['productname']:
        if i in  dataprdname:
            print(i)
            pos = dataprdname.index(i)
            print(pos)
            datarate.append(dataprd['productrate'][pos])
    print(datarate)
    total=0
    for  i in range(len(datarate)):
            total+=datarate[i]*datacart['productqut'][i]
    print(total)
    
   


  

            
        




                
                


            









