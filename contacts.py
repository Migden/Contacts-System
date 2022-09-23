
import sys
import sqlite3
from time import sleep
import os

4/10

help_menu = '''
    add -- make new contact entry
    search -- search using key words or filters
    dump -- shows all contacts in the database
    change -- change message by id classification
    remove -- removes contact by id filtering
    help -- prints help menu
    clear -- clears terminal
'''

run = True
starting = '''
  ______                                         _____                  _                      
 / _____)           _               _           (____ \       _        | |                     
| /      ___  ____ | |_  ____  ____| |_   ___    _   \ \ ____| |_  ____| | _   ____  ___  ____ 
| |     / _ \|  _ \|  _)/ _  |/ ___)  _) /___)  | |   | / _  |  _)/ _  | || \ / _  |/___)/ _  )
| \____| |_| | | | | |_( ( | ( (___| |__|___ |  | |__/ ( ( | | |_( ( | | |_) | ( | |___ ( (/ / 
 \______)___/|_| |_|\___)_||_|\____)\___|___/   |_____/ \_||_|\___)_||_|____/ \_||_(___/ \____)
 
    add -- make new contact entry
    search -- search using key words or filters
    dump -- shows all contacts in the database
    change -- change message by id classification
    remove -- removes contact by id filtering
    help -- prints help menu
    clear -- clears terminal
 ______________________________________________________________________________________________\n\n'''

def sprint(word):  ## Function sprint give the text passed as a parameter a typewriter look
    for letter in word:
        sleep(0.000001)
        sys.stdout.write(letter)
        sys.stdout.flush()


conn = sqlite3.connect('conntact.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME            TEXT    NOT NULL,
    EMAIL           TEXT    NOT NULL,
    PHONE           TEXT    NOT NULL);''');

conn.commit()

def add_contacts():  ## add_contacts function takes name, email and phone arguments and then adds them to a row in the contacts table in the database
    name1 = input("Enter contact name: ")
    email1 = input("Enter contact email: ")
    phone1 = input("Enter contact phone number: ")
    cursor.execute("INSERT INTO contacts (ID, NAME,EMAIL,PHONE) VALUES (?,?,?,?)", (None, name1, email1, phone1));
    conn.commit()


def change():
    id_filter = input("Enter id of contact you want to change: ")
    sprint('Catergories you can change -- Name -- Email -- Phone\n')
    choice = input('Enter catergory >> ')
    if choice.lower() == 'name':
        change = input("Enter new Name: ")
        cursor.execute("UPDATE contacts SET NAME = (?) WHERE ID = (?)", (change, id_filter))
        conn.commit()
    elif choice.lower() == 'email':
        change = input("Enter new Email: ")
        cursor.execute(f'UPDATE contacts SET EMAIL = (?) WHERE ID = (?', (change, id_filter))
        conn.commit()
    elif choice.lower() == 'phone':
        change = input("Enter new Phone: ")
        cursor.execute(f'UPDATE contacts SET EMAIL = (?) WHERE ID = (?)', (change, id_filter))




def read_all_contact():
    cursor.execute("SELECT * FROM contacts");
    records = cursor.fetchall()
    for row in records:
        print(f'\nId: {row[0]}')
        print(f'Name: {row[1]}')
        print(f'Email: {row[2]}')
        print(f'Phone: {row[3]}\n')
        print("_______________________________\n")



'''
The filter_contacts function allows user to chose the contact filtering method

'''
def filter_contacts():
    choice = str(input("Enter which caterorgy of search filtering name/email/phone: "))
    if choice == 'name':
        name_filter = input("Enter name: ")
        records1 = cursor.execute(f"SELECT * FROM contacts WHERE NAME LIKE '{name_filter}%'");
        for row in records1:
            print(f'Id: {row[0]}')
            print(f'Name: {row[1]}')
            print(f'Email: {row[2]}')
            print(f'Phone: {row[3]}\n')

    elif choice == 'email':
        email_filter = input("Enter email: ")
        records1 = cursor.execute(f"SELECT * FROM contacts WHERE EMAIL LIKE '{email_filter}%'");
        for row in records1:
            print(f'Id: {row[0]}')
            print(f'Name: {row[1]}')
            print(f'Email: {row[2]}')
            print(f'Phone: {row[3]}\n')

    elif choice == 'phone':
        phone_filter = input("Enter phone: ")
        records1 = cursor.execute(f"SELECT * FROM contacts WHERE PHONE LIKE '{phone_filter}%'");
        for row in records1:
            print(f'Id: {row[0]}')
            print(f'Name: {row[1]}')
            print(f'Email: {row[2]}')
            print(f'Phone: {row[3]}\n')           

def delete(): ## Delete function takes in an id and then removes the row from the database table
    delete = int(input("Enter id to remove: "))
    cursor.execute(f"DELETE FROM contacts WHERE ID = {delete}");
    conn.commit()

    
def main():
    sprint(starting)
    while run:          ## While loop added to forever run through code to give a terminal effect
        command = input(f"root@kali > ")
        if command.lower() == 'add':
            add_contacts()
        elif command.lower() == 'search':
            filter_contacts()
        elif command.lower() == 'dump':
            read_all_contact()
        elif command.lower() == 'clear':
            os.system('cls')
        elif command.lower() == 'remove':
            delete()
        elif command.lower() == 'help':
            print(help_menu)
        elif command.lower() == 'change':
            change()
        elif command.lower() == 'exit':
            sys.quit()



if __name__ == '__main__':
    main()



