from django.db import connection
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql1234",
    database = "sqldb"
)

mycursor = connection.cursor()

