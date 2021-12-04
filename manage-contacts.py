from app import Contact, db, contacts_schema
from flask import request

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
    contact = Contact.query.get_or_404(selected_id)
    if selected_id == str(contact.id):
        print("Fist Name: " + contact.first_name)
        print("Last Name: " + contact.last_name)
        print("Email: " + contact.email)
        print("Phone Number: " + contact.phone_number)
    else:
        print("Contact not found!")

elif option == "3":
    f_name = input("Enter First Name: ")
    l_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    phone_nr = input("Enter Phone Number: ")

    contact = Contact(first_name=f_name, last_name=l_name, email=email, phone_number=phone_nr)
    db.session.add(contact)
    db.session.commit()

# elif option == "4":
#     selected_id = input("Enter contact ID to UPDATE: ")
#     contact = Contact.query.get_or_404(selected_id)
#     print("Fist Name: " + contact.first_name)
#     print("Last Name: " + contact.last_name)
#     print("Email: " + contact.email)
#     print("Phone Number: " + contact.phone_number)
    # f_name = input("Enter First Name: ")
    # l_name = input("Enter Last Name: ")
    # email = input("Enter Email: ")
    # phone_nr = input("Enter Phone Number: ")
    # updated_contact = Contact(first_name=f_name, last_name=l_name, email=email, phone_number=phone_nr)
    # db.session.update(updated_contact)
    # db.session.commit()

elif option == "5":
    selected_id = input("Enter contact ID to DELETE: ")
    contact = Contact.query.get_or_404(selected_id)
    db.session.delete(contact)
    db.session.commit()
    print(f'Contact {contact.first_name} deleted')
