from app import Contact, db, contacts_schema

print("1 to view all contacts")
print("2 to create a contact")
print("3 to delete by ID")
print("")
print("")
option = input("Select option: ")

if option == "1":
    print("You have selected option 1")
elif option == "2":
    f_name = input("Enter First Name: ")
    l_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    phone_nr = input("Enter Phone Number: ")

    contact = Contact(first_name=f_name, last_name=l_name, email=email, phone_number=phone_nr)
    db.session.add(contact)
    db.session.commit()
elif option == "3":
    selected_id = input("Enter selected id to delete: ")
    contact = Contact.query.get_or_404(selected_id)
    db.session.delete(contact)
    db.session.commit()
    print(f'Contact {contact.first_name} deleted')