
from save import save_all

def add_contact(all_contacts):
    name=str(input("Enter Person Name  :").strip())
    email=str(input("Enter Person E-Mail address  :").strip())
    phone=int(input("Enter Person Mobile Number  :").strip())
    if not phone.isdigit():
        print("phone number must be integer")
        return all_contacts

    address=str(input("Enter Person contact address   :").strip())

    for contact in all_contacts:
        if contact['phone']==phone:
            print("can't accept duplicate phn number")
            return all_contacts

    # take input and directly stores to dictionary
    dic={
        "Name":name,
        "Email":email,
        "phone":phone,
        "address":address}
    all_contacts.append(dic)
    save_all(all_contacts)

    print('contacts added succesfully')

    return all_contacts

 




