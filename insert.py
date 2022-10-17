import mysql.connector
from connection import connection,mycursor
def insertProduct(list):
    sql = "INSERT INTO sqltable(\
            Name,Surname,Note_1,Note_2,Final_Note,Photo,Description)\
            VALUES(%s,%s,%s,%s,%s,%s,%s)"


    value = list

    mycursor.execute(sql,value)

    try:
        connection.commit()
        print("your record has been saved {}".format(mycursor.rowcount))

    except mysql.connector.Error as er:
        print(f"Your Error is {er}")

    finally:
        connection.close()
        print("your database closed")


def insertProducts(list):
    sql = "INSERT INTO sqltable(\
            Name,Surname,Note_1,Note_2,Final_Note,Photo,Description)\
            VALUES(%s,%s,%s,%s,%s,%s,%s)"
    values = list

    mycursor.executemany(sql,values)

    try:
        connection.commit()
    except mysql.connector.Error as er:
        print("er")

    finally:
        connection.close()
        print("your database closed")

list = []
while True:
    name = input("Name: ")
    surname = input("Surname: ")
    try:
        note_1 = int(input("Note 1: "))
        note_2 = int(input("Note 2: "))
        final_note = int(input("Final Note: "))
    except Error as er:   #look raise method
        print("enter a numeric value")

    photo = input("Student Photo: ")
    description = input("Student Description: ")
    list.append((name,surname,note_1,note_2,final_note,photo,description))
    #add raise method
    answer = input("Do you want to add new student: (y/n)")
    if answer == "n":
        break
