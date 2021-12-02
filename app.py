from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


#### Models ####
class Contact(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(10))

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

class ContactListResource(Resource):
    #### CRUD - GET (READ) ####
    def get(self):
        contacts = Contact.query.all()
        return contacts_schema.dump(contacts)

    #### CRUD - ADD (CREATE) ####
    def post(self):
        new_contact = Contact(
            first_name=request.json['first_name'],
            last_name=request.json['last_name'],
            email=request.json['email'],
            phone_number=request.json['phone_number']
        )
        db.session.add(new_contact)
        db.session.commit()
        return contact_schema.dump(new_contact)

api.add_resource(ContactListResource, '/contacts')


class ContactResource(Resource):
    """ Fetching a single record by ID """
    def get(self, contact_id):
        contact = Contact.query.get_or_404(contact_id)
        return contact_schema.dump(contact)

    #### CRUD - PATCH (UPDATE) ####
    def patch(self, contact_id):
        contact = Contact.query.get_or_404(contact_id)

        if 'first_name' in request.json:
            contact.first_name = request.json['first_name']
        if 'last_name' in request.json:
            contact.last_name = request.json['last_name']
        if 'email' in request.json:
            contact.email = request.json['email']
        if 'phone_number' in request.json:
            contact.phone_number = request.json['phone_number']

        db.session.commit()
        return contact_schema.dump(contact)

    #### CRUD - DELETE (DELETE) ####
    def delete(self, contact_id):
        contact = Contact.query.get_or_404(contact_id)
        db.session.delete(contact)
        db.session.commit()
        return '', 204

api.add_resource(ContactResource, '/contacts/<int:contact_id>')

if __name__ == '__main__':
    app.run(debug=True)
