
def save_all(all_contacts):
    with open('contact.csv','w') as file:
        for contact in all_contacts:
            line=f"{contact['Name']},{contact['Email']}, {contact['phone']}, {contact['address']}\n"
            file.write(line)

