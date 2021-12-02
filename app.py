from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://sql4455717:Sa8jeBNmvl@sql4.freemysqlhosting.net:3306/sql4455717'
db = SQLAlchemy(app)
