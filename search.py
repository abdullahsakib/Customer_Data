

def search_value(value):
    try:
        with open('contact.csv','r') as file:
            lines=file.readlines()

            #value='we'
            found_lines=[]
            for index,line in enumerate(lines, start=1):
                #print(index,line)
                if value in line:
                    found_lines.append([index,line.strip().split(',')])
            
            for line in found_lines:
                print(f"Find in Line no-> {line[0]}, contact info:-> Name: {line[1][0]}, E-Mail: {line[1][1]},  Phone: {line[1][2]}, Address: {line[1][3]}")
    
    except Exception as e:
        print(e)
