from flask import Flask
from flask_restful import reqparse, Api, Resource
from flask-mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'sql4455717'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = 'sql4.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql4455717'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)