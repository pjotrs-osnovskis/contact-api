from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)


#### Models ####
class Contact(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(10))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    def __init__(self,first_name,last_name,email,phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
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

#### CRUD Functionality ####
#### CRUD - READ / GET ####
@app.route('/contacts', methods = ['GET'])
def index():
    get_contacts = Contact.query.all()
    contact_schema = ContactSchema(many=True)
    contacts = contact_schema.dump(get_contacts)
    return make_response(jsonify({"contact": contacts}))


if __name__ == '__main__':
    app.run(debug=True)