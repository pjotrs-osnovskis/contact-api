from enum import unique
from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates 
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
import os
if os.path.exists("env.py"):
    import env
from sqlalchemy.orm import validates
import re 
    
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get("DB_URL")
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


#### Models ####
class Contact(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(), index=True, nullable=False)
    last_name = db.Column(db.String(), index=True, nullable=False)
    email = db.Column(db.String(), index=True, nullable=False)
    phone_number = db.Column(db.String(13), index=True, nullable=False)
    
    @validates('first_name') 
    def validate_first_name(self, key, first_name):
        if not first_name:
            raise AssertionError('No first name provided')
        if len(first_name) < 3 or len(first_name) > 20:
            raise AssertionError('First name must be between 3 and 20 characters')
        return first_name
    
    @validates('last_name') 
    def validate_last_name(self, key, last_name):
        if not last_name:
            raise AssertionError('No last name provided')
        if len(last_name) < 3 or len(last_name) > 20:
            raise AssertionError('Last name must be between 3 and 20 characters')
        return last_name

    @validates('email') 
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('No email provided')
        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Please enter correct email')
        if Contact.query.filter(Contact.email == email).first():
            raise AssertionError('Email is already in use')
        return email

    @validates('phone_number') 
    def validate_phone_number(self, key, phone_number):
        validate = "r'^(?:\+?0044)?[007]\d{9,15}$'"
        if not phone_number:
            raise AssertionError('No phone number provided')
        if len(phone_number) < 9 or len(phone_number) > 15:
            raise AssertionError('(C1) Enter correct phone number, following inner UK standard (07) or International (0044)')
        if re.search(validate, phone_number):
            raise AssertionError('(C2) Enter correct phone number, following inner UK standard (07) or International (0044)') 

        return phone_number

    def __repr__(self):
        return '' % self.id
db.create_all()


#### Model Schema ####
class ContactSchema(ma.Schema):
    class Meta():
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number')

contact_schema = ContactSchema()
contacts_schema = ContactSchema(many=True)


#### CRUD - GET (READ) ####
def get_contacts():
    contacts = Contact.query.all()
    return contacts_schema.dump(contacts)


#### CRUD - GET BY ID (GET) ####
def get_contact_by_id(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    return contact_schema.dump(contact)


#### CRUD - ADD (CREATE) ####
def add_contact(contact):
    contact = Contact(
        first_name=request.args['first_name'],
        last_name=request.args['last_name'],
        email=request.args['email'],
        phone_number=request.args['phone_number']
    )

    db.session.add(contact)
    db.session.commit()
    return contact_schema.dump(contact)


#### CRUD - PUT (UPDATE) ####
def update_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)

    if 'first_name' in request.args:
        contact.first_name = request.args['first_name']
    if 'last_name' in request.args:
        contact.last_name = request.args['last_name']
    if 'email' in request.args:
        contact.email = request.args['email']
    if 'phone_number' in request.args:
        contact.phone_number = request.args['phone_number']

    db.session.commit()
    return contact_schema.dump(contact)


#### CRUD - DELETE (DELETE) ####
def delete_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    return '', 204


######### API ROUTES #########

#### CRUD - GET (READ) ####
@app.route('/api/contacts', methods=['GET'])
def api_get_contacts():
    return jsonify(get_contacts())


#### CRUD - GET BY ID (READ) ####
@app.route('/api/contacts/<contact_id>', methods=['GET'])
def api_get_contact(contact_id):
    return jsonify(get_contact_by_id(contact_id))


#### CRUD - ADD (CREATE) ####
@app.route('/api/contacts/add',  methods = ['POST'])
def api_add_contact():
    contact = request.get_json()
    return jsonify(add_contact(contact))


#### CRUD - PUT (UPDATE) ####
@app.route('/api/contacts/update/<contact_id>',  methods = ['PUT'])
def api_update_contact(contact_id):
    return jsonify(update_contact(contact_id))

@app.route('/api/contacts/delete/<contact_id>',  methods = ['DELETE'])
def api_delete_contact(contact_id):
    return jsonify(delete_contact(contact_id))


if __name__ == '__main__':
    app.run(debug=True)
