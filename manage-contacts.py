from app import Contact, db, contacts_schema

def mainmenu():
    print("")
    print("========= MAIN MENU ==========")
    print("1 to VIEW ALL contacts")
    print("2 to SHOW contact by ID")
    print("3 to CREATE a contact")
    print("4 to UPDATE contact by ID")
    print("5 to DELETE contact by ID")
    print("6 to EXIT")
    option = input("Select option: ")

    if option == "1":
        contacts = contacts_schema.dump(Contact.query.all())
        for c in contacts:
            print("")
            print(f"Name: {c['first_name']} {c['last_name']}")
            print(f"Email: {c['email']}")
            print(f"Phone number: {c['phone_number']}")
            print(f"ID: {c['id']}")
        mainmenu()

    elif option == "2":
        selected_id = input("Enter contact ID to view: ")
        try:
            contact = Contact.query.get_or_404(selected_id)
            print("")
            print(f"====== {contact.first_name}'s Contact ======")
            print(f"Name: {contact.first_name} {contact.last_name}")
            print(f"Email: {contact.email}")
            print(f"Phone number: {contact.phone_number}")
            print(f"ID: {contact.id}")
            go_back = input("Press ENTER to go back.")
            if go_back or go_back == "":
                mainmenu()
        except:
            print("Contact not found!")
            print("")
            mainmenu()

    elif option == "3":
        f_name = input("Enter First Name: ")
        l_name = input("Enter Last Name: ")
        email = input("Enter Email: ")
        phone_nr = input("Enter Phone Number: ")

        contact = Contact(first_name=f_name, last_name=l_name, email=email, phone_number=phone_nr)
        db.session.add(contact)
        db.session.commit()
        print("")
        print("Contact added Successfully!")
        print("")
        print("Fist Name: " + contact.first_name)
        print("Last Name: " + contact.last_name)
        print("Email: " + contact.email)
        print("Phone Number: " + contact.phone_number)
        print("")
        mainmenu()

    elif option == "4":
        selected_id = input("Enter contact ID to UPDATE: ")
        try:
            contact = Contact.query.get_or_404(selected_id)
            print("Selected contact: ")
            print("Fist Name: " + contact.first_name)
            print("Last Name: " + contact.last_name)
            print("Email: " + contact.email)
            print("Phone Number: " + contact.phone_number)
            print("")
            print("Enter new information:")
            contact.first_name = input("Enter First Name: ")
            contact.last_name = input("Enter Last Name: ")
            contact.email = input("Enter Email: ")
            contact.phone_number = input("Enter Phone Number: ")
            db.session.commit()
            print("")
            print("Update Successful!")
            mainmenu()

        except:
            print("Contact not found!")


    elif option == "5":
        selected_id = input("Enter contact ID to DELETE: ")
        try:
            contact = Contact.query.get_or_404(selected_id)
            db.session.delete(contact)
            db.session.commit()
            print("")
            print(f'Contact {contact.first_name} deleted!')
            mainmenu()

        except:
            print("Contact not found!")

    elif option == "6":
        exit()

    else:
        print("")
        print("Please select one of the menu options!")
        mainmenu()
mainmenu()
