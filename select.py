
from connection import connection,mycursor

def getProduct():
    sql = 'SELECT * FROM sqltable'
    mycursor.execute(sql)
    table = mycursor.fetchone()

    return table
def getProducts():
    sql = 'SELECT * FROM sqltable'
    mycursor.execute(sql)
    table = mycursor.fetchall()
    return table
def getFilter(description):
    sql = f"SELECT * FROM sqltable where Description = '{description}'"
    mycursor.execute(sql)
    table = mycursor.fetchall()
    return table
def getFilterAvrNOte():
    mycursor.execute("SELECT Note_1,Note_2,Final_Note FROM sqltable")
    table = mycursor.fetchall()
    list = []
    for i in table:
        avr = (i[0]+i[1]+i[2])/3
        list.append(avr)
    return list
        
def aggregatea():   #---debriefing
    pass