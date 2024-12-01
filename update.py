


def promt_updates(fields):
    name=input(f"Update name (current {fields[0]} ): ").strip() or fields[0]
    email = input(f"Update E-Mail (current: {fields[1]}): ").strip() or fields[1]
    phone = input(f"Update Phone (current: {fields[2]}): ").strip() or fields[2]
    address = input(f"Update Address (current: {fields[3]}): ").strip() or fields[3]

    return [name, email, phone, address]

def update_contact(item):
    try:
        with open('contact.csv','r') as file:
            lines=file.readlines()

        updated_line=[]
        found=False

        #item=input("value")

        for index, line in enumerate(lines):
            fields=line.strip().split(',')
            #print(fields)
            if item.isdigit():
                if index==int(item):
                    found=True
                    print(f'found line->{item}')
                    fields=promt_updates(fields)
                updated_line.append(','.join(fields)+'\n')
            else:
                if fields and fields[0]==item:
                    print(f'found name ->{item}')
                    found=True
                    fields=promt_updates(fields)
                updated_line.append(','.join(fields)+'\n')

                

        if not found:
            print(f" no match found for {item}")

        if found:
            with open('contact.csv','w') as wfile:
                wfile.writelines(updated_line)
            print(f"The record for {item} updates succesfully")
    except Exception as e:
        print(f"Error: {e}")


   






    
        



