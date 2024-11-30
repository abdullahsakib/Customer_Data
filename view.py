
import csv

def view_all_contacts():
    try:
        with open('contact.csv','r') as file:
            csv_reader=csv.reader(file)
            for file in csv_reader:
                print(file)
    except:
        print("""Soory No value Found \nInput value first""")