from app import app
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

# CRUD operation: ADD
@app.route('/add', methods=['POST'])
def add_contact():
    try:
        # Adding contact name, email and phone number to variables to use in SQL Query and send to database
        json = request.json
        Contact_name = json['contact_name']
        Contact_email = json['contact_email']
        Contact_phone_number = json['contact_phone_number']
        if Contact_name and Contact_email and Contact_phone_number and request.method == 'POST':
            SQL_Query = "INSERT INTO contacts(Contact_name, Contact_email, Contact_phone_number) VALUES(%s, %s, %s)"
            data = (Contact_name, Contact_email, Contact_phone_number,)
            connection = MySQL.connection()
            Pointer = connection.cursor()
            Pointer.execute(SQL_Query, data)
            connection.commit()
            response = jsonify('Contact added!')
            response.status_code = 200
            return response
        else:
            return not_found()
    except Exception as e:
        # Printing out an error in terminal if any occurs
        print(e)
    finally:
        # Closing the connection
        Pointer.close() 
        connection.close()


if __name__ == "__main__":
    app.run()