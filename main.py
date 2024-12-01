from add import add_contact
from view import view_all_contacts
from search import search_value
from delete import delete_contact
from update import update_contact

all_contacts=[]

while True:
    print("Welcome Contact Book Management System")
    print("0 -> if you wanna exit")
    print("1 -> to add Contact")
    print("2 -> to view Contact")
    print("3 -> to search value")
    print("4 -> to delete Contact")
    print("5 -> to update Contact")


    menu=input('Select any number from 0 to 5 :->')

    if menu=="0":
        print("Thanks for using Contact Book Management System ")
        break
    elif menu=="1":
        all_contacts=add_contact(all_contacts)

    elif menu=="2":
        view_all_contacts()

    elif menu=="3":
        search_value(input('Which word to find ?'))

    elif menu=="4":
        item = input("Enter the line number or contact name of the contact you want to delete?  :")
        delete_contact(item)
    
    elif menu=="5":
        item = input("Enter the line number or contact name of the contact you want to update?  :")
        update_contact(item)

    else:
        print('select a valid number')