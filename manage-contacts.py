from app import Contact, db, contacts_schema

print("1 to VIEW ALL contacts")
print("2 to SHOW contact by ID")
print("3 to CREATE a contact")
print("4 to UPDATE contact by ID")
print("5 to DELETE contact by ID")
option = input("Select option: ")

if option == "1":
    contacts = Contact.query.all()
    print(contacts_schema.dump(contacts))

elif option == "2":
    selected_id = input("Enter contact ID to view: ")
    try:
        contact = Contact.query.get(selected_id)
        print("Fist Name: " + contact.first_name)
        print("Last Name: " + contact.last_name)
        print("Email: " + contact.email)
        print("Phone Number: " + contact.phone_number)
    except:
        print("Contact not found!")

elif option == "3":
    f_name = input("Enter First Name: ")
    l_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    phone_nr = input("Enter Phone Number: ")

    contact = Contact(first_name=f_name, last_name=l_name, email=email, phone_number=phone_nr)
    db.session.add(contact)
    db.session.commit()

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
    except:
        print("Contact not found!")


elif option == "5":
    selected_id = input("Enter contact ID to DELETE: ")
    try:
        contact = Contact.query.get_or_404(selected_id)
        db.session.delete(contact)
        db.session.commit()
        print(f'Contact {contact.first_name} deleted')
    except:
        print("Contact not found!")

else:
    print("Wrong option selected.")

