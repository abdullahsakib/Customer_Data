


def add_contact():
    name=str(input("Enter Person Name"))
    email=str(input("Enter Person E-Mail adress"))
    phone=int(input("Enter Person Mobile Number"))
    adress=str(input("Enter Person contact adress"))
    dic={}

    # dic={
    #     "Name":name,
    #     "Email":email,
    #     "phone":phone,
    #     "adress":adress}
    dic["Name"]=name
    dic["Email"]=email
    dic["phone"]=phone
    dic['adress']=adress

    print(dic)




