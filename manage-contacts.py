from app import Contact, db

f_name = input("Enter First Name: ")
l_name = input("Enter Last Name: ")
email = input("Enter Email: ")
phone_nr = input("Enter Phone Number: ")

contact = Contact(first_name=f_name, last_name=l_name, email=email, phone_number=phone_nr)
db.session.add(contact)
db.session.commit()