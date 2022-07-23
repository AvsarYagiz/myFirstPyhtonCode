import random

contact = {}


def add_contact(name, phone):
    global contact
    if name not in contact.keys():
        contact[name] = phone
    else:
        print("The person you want to add already exist!")


def delete_contact(name):
    global contact
    try:
        del contact[name]
    except KeyError:
        print("The person you want to delete already does not exist!")


def update_contact_name(name, rename):
    global contact
    if name in contact.keys():
        if rename not in contact.keys():
            contact[rename] = contact[name]
            del contact[name]
            print("The name was updated successfully!")
    else:
        print("The person you want to update does not exist!")


def update_contact_phone(name, renumber):
    global contact
    if name in contact.keys():
        contact[name] = renumber
        print("The phone number was updated successfully!")
    else:
        print("The person you want to update does not exist!")


"""
def random_choice():
    name = random.choice(list(contact.keys()))
    return name, contact[name]
    """


def view_contacts():
    global contact
    if not len(contact) == 0:
        print("Contacts:\n")
        i = 1
        for key, value in contact.items():
            print(f"{i})\n\tName: {key}\n\tPhone number: {value}")
            i += 1
        return
    print("The contacts are empty!")


def main():
    global contact
    menu = '''
     _________________________
     | 1: Add Contact |
     | 2: Delete Contact |
     | 3: Update Name |
     | 4: Update Phone |
     | 5: Random Contact | 
     | 6: Show All Contacts |
     | q: Exit |
     _________________________
     '''
    print(menu)
    while True:
        selection = input("Please make a choise:  ")
        print("*" * 50 + "\n")
        if selection == "1":
            name = input("Enter name for new contact: ")
            phone = input("Enter phone number for new contact: ")
            add_contact(name, phone)
        elif selection == "2":
            name = input("Enter the name of contact that you wish delete ")
            delete_contact(name)
        elif selection == "3":
            name = input("Enter the name you wish change: ")
            rename = input("Enter the new name: ")
            update_contact_name(name, rename)
        elif selection == "4":
            name = input("Enter the name of contact that you wish change it phone number: ")
            renumber = input("Enter the new phone number: ")
            update_contact_phone(name, renumber)

        elif selection == "5":
            name = random.choice(list(contact.keys()))
            phone = contact[name]
            print(f"\n\tName: {name}\n\tPhone: {phone}")

        elif selection == "6":
            view_contacts()

        elif selection == "q":
            break

        else:
            print("You have made an invalid choice. Please try again!")
        print(menu)


main()
