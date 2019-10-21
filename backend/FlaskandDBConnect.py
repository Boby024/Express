from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app= Flask(__name__)

app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'Bob'
app.config['MYSQL_PASSWORD']= 'Iamusing24@'
app.config['MYSQL_DB']= 'anzeige'
mysql= MySQL(app)
