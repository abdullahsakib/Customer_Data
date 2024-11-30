from add import add_contact

all_contacts=[]

while True:
    print("Welcome Contact Book Management System")
    print("0 -> if you wanna exit")
    print("1 -> to add Contact")
    print("2 -> to view Contact")
    print("3 -> to update value")
    print("4 -> to delete Contact")

    menu=input('Select any number from 0 to 4')

    if menu=="0":
        print("Thanks for using Contact Book Management System ")
        break
    elif menu=="1":
        all_contacts=add_contact(all_contacts)
        # pass
        # all_books=add_contact(all_books)
    # elif menu=="2":
    #     view_all_books(all_books)
    # elif menu=="3":
    #     line=int(input("enter line no"))
    #     update(all_books,line)

    # elif menu=="4":
    #     line = int(input("Enter the line number of the book you want to delete"))
    #     delete(all_books,line)

    else:
        print('select a valid number')