
from save import save_all

def add_contact(all_contacts):
    name=str(input("Enter Person Name  :"))
    email=str(input("Enter Person E-Mail address  :"))
    phone=int(input("Enter Person Mobile Number  :"))
    address=str(input("Enter Person contact address   :"))


    # take input and directly stores to dictionary
    dic={
        "Name":name,
        "Email":email,
        "phone":phone,
        "adress":address}
    all_contacts.append(dic)
    save_all(all_contacts)

    print('contacts added succesfully')

    return all_contacts
    
 




