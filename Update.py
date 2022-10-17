import mysql.connector
from connection import connection,mycursor

def updateProduct(name,surname,id):
    sql = f"Update sqltable Set Name='{name}', Surname ='{surname}' where id = '{id}'"

    mycursor.execute(sql)
    try:
        connection.commit()
        print(f"{mycursor.rowcount} update table")

    except mysql.connector.Error as err:
        print("Error",err)
    finally:
        connection.close()
        print("closed Database")

def Menü():
    id = input("Which record would you like to change?")
    name = input("name")
    surname  = input("surname")
    updateProduct(name,surname,id)
     
