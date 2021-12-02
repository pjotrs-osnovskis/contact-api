# INSTRUCTIONS FOR CONTACT-API

## CMD

Use next command in your CMD to **GET** all records from database:

`curl http://127.0.0.1:5000/contacts -i -H "Content-Type: application/json" -X GET`

Use next command in your CMD to **GET** individual record by id from database:

`curl http://127.0.0.1:5000/contacts/<id> -i -H "Content-Type: application/json" -X GET`

Use next command in your CMD to **CREATE** individual record by id from database:

`curl http://127.0.0.1:5000/contacts -i -H "Content-Type: application/json" -X POST -d "{\"first_name\":\"<First Name>\", \"last_name\":\"<Last Name>\", \"email\":\"<Email>\", \"phone_number\":\"<Phone Number>\"}"`

Use next command in your CMD to **UPDATE** individual record by id from database:

`curl http://127.0.0.1:5000/contacts/<id> -i -H "Content-Type: application/json" -X PATCH -d "{\"first_name\":\"<First Name>\", \"last_name\":\"<Last Name>\", \"email\":\"<Email>\", \"phone_number\":\"<Phone Number>\"}"`

Use next command in your CMD to **DELETE** individual record by id from database:

`curl http://127.0.0.1:5000/contacts/<id> -X DELETE -I`



> `<id>` - unique id of a contact record (integer)

> `<First Name>` - enter fist name of a contact (string)

> `<Last Name>` - enter last name of a contact (string)

> `<Email>` - enter contact's email address (string)

> `<Phone Number>` - enter contact's phone number (string)


