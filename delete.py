

def delete_contact(item):
    with open('contact.csv','r') as file:
        lines=file.readlines()
    
    updated_line=[]
    found=False

    if item.isdigit():
        line_remove=int(item)
        for index, line in enumerate(lines):
            if index==line_remove:
                print(f"Removing line {line_remove} : {line.strip()}")
                found=True
            else:
                updated_line.append(line)
    else:
        for line in lines:
            fields=line.strip().split(',')
            if fields and fields[0]==item:
                print(f"Removing contact for name {item} : {line.strip()}")
                found=True
            else:
                updated_line.append(line)

    
    with open('contact.csv', 'w') as file:
        file.writelines(updated_line)
    





