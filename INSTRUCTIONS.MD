# INSTRUCTIONS FOR CONTACT-API

<br>


## VIRTUAL ENVIRONMENT

Easiest way to create virtual environment is yo use **venv**.
In your terminal cd to app's path and run next command:
`python -m venv venv`.

To activate it run `venv\Scripts\activate.bat`, to deactivate, simply type `deactivate` in terminal prompt.

<br>

---

## CREATING A DATABASE

Register on [freemysqlhosting.net](freemysqlhosting.net), create `env.py` file in app's root directory.
```
import os

os.environ.setdefault("DB_URL", "mysql+pymysql://<username>:<password>@<hosting>:<port>/<dbname>")

```

<br>

---
##  ACCESS DATABASE VIA URL

To access database records run `python app.py`, then visit [http://127.0.0.1:5000/api/contacts](http://127.0.0.1:5000/api/contacts).

<br>

---

## REST API IMPLEMENTATION

| # | Endpoints                                                | HTTP Method | Description                              | DB Function                   |
|:-:| -------------------------------------------------------- | ----------- | ---------------------------------------- | ----------------------------- |
| 1 | `http://127.0.0.1:5000/api/contacts`                     | GET         | Get the list of all contacts in DB       | get_contacts()                |
| 2 | `http://127.0.0.1:5000/api/contacts/<contact_id>`        | GET         | Get a single contact from DB             | get_contact_by_id(contact_id) |
| 3 | `http://127.0.0.1:5000/api/contacts/add`                 | POST        | Add a single contact to DB               | add_contact(contact)          |
| 4 | `http://127.0.0.1:5000/api/contacts/update/<contact_id>` | PUT         | Update a single contact from DB          | update_contact(contact_id)    |
| 5 | `http://127.0.0.1:5000/api/contacts/delete/<contact_id>` | DELETE      | Delete a single contact from DB          | delete_contact(contact_id)    |

<br>

---

## TERMINAL PROGRAM

Run `python manage-contacts.py` to Create, Read, Update and Delete contacts via terminal program.


<br>

---

## CMD

Use next command in your CMD to **GET** all records from database:

`curl http://127.0.0.1:5000/api/contacts -i -H "Content-Type: application/json" -X GET`

Use next command in your CMD to **GET** individual record by id from database:

`curl http://127.0.0.1:5000/api/contacts/<id> -i -H "Content-Type: application/json" -X GET`

Use next command in your CMD to **CREATE** individual record by id from database:

`curl http://127.0.0.1:5000/api/contacts -i -H "Content-Type: application/json" -X POST -d "{\"first_name\":\"<First Name>\", \"last_name\":\"<Last Name>\", \"email\":\"<Email>\", \"phone_number\":\"<Phone Number>\"}"`

Use next command in your CMD to **UPDATE** individual record by id from database:

`curl http://127.0.0.1:5000/api/contacts/<id> -i -H "Content-Type: application/json" -X PATCH -d "{\"first_name\":\"<First Name>\", \"last_name\":\"<Last Name>\", \"email\":\"<Email>\", \"phone_number\":\"<Phone Number>\"}"`

Use next command in your CMD to **DELETE** individual record by id from database:

`curl http://127.0.0.1:5000/api/contacts/<id> -X DELETE -I`



> `<id>` - unique id of a contact record (integer)

> `<First Name>` - enter fist name of a contact (string)

> `<Last Name>` - enter last name of a contact (string)

> `<Email>` - enter contact's email address (string)

> `<Phone Number>` - enter contact's phone number (string)


