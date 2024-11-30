from add import add_contact
from view import view_all_contacts
from search import search_value

all_contacts=[]

while True:
    print("Welcome Contact Book Management System")
    print("0 -> if you wanna exit")
    print("1 -> to add Contact")
    print("2 -> to view Contact")
    print("3 -> to search value")
    print("4 -> to delete Contact")

    menu=input('Select any number from 0 to 4   :')

    if menu=="0":
        print("Thanks for using Contact Book Management System ")
        break
    elif menu=="1":
        all_contacts=add_contact(all_contacts)

    elif menu=="2":
        view_all_contacts()
    elif menu=="3":
        search_value(input('Which word to find ?'))
    #     line=int(input("enter line no"))
    #     update(all_books,line)

    # elif menu=="4":
    #     line = int(input("Enter the line number of the book you want to delete"))
    #     delete(all_books,line)

    else:
        print('select a valid number')