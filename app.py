from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://sql4455717:Sa8jeBNmvl@sql4.freemysqlhosting.net:3306/sql4455717'
db = SQLAlchemy(app)


###Models####
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

