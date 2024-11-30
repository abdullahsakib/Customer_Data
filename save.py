
def save_all(all_contatcs):
    with open('contact.csv','w') as file:
        for contact in all_contatcs:
            line=f"{contact['Name']},contact['Email']}, contact['phone']}, contact['address']}"
            file.write(line)

