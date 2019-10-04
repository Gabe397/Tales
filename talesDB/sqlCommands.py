import mysql.connector

cnx = mysql.connector.connect(user='root',password='password',host='127.0.0.1',database ='logDB')

if(cnx):
    print("Connected")
else:
    print("HAH you woulda thought")


def insertLog(email,passwd):
    dbCursor = cnx.cursor()

    chksql = """SELECT * FROM logs WHERE email = '%s' AND password = '%s' """ %(email,passwd)

    dbCursor.execute(chksql)

    chkresult = dbCursor.fetchall()
    
    if len(chkresult) == 0:
        insql = "INSERT INTO logs (email, password) VALUES(%s,%s)"
        val = (email,passwd)

        dbCursor.execute(insql,val)

        cnx.commit()

        print(dbCursor.rowcount, "Record Inserted")
    else:
        print("Account Exists")

    cnx.close()

def auth(email,passwd):

    dbCursor = cnx.cursor()

    sql = """SELECT * FROM logs WHERE email = '%s' AND password = '%s' """ %(email,passwd)

    dbCursor.execute(sql)

    myresult = dbCursor.fetchall()

    if len(myresult) == 0:
        print("Failed Authentification")
    
    elif len(myresult) == 1:
        print("You're connected")

    cnx.close()


def getLog(email,passwd):
    dbCursor = cnx.cursor()

    sql = """SELECT * FROM logs WHERE email = '%s' AND password = '%s' """ %(email,passwd)

    dbCursor.execute(sql)

    myresult = dbCursor.fetchall()

    if len(myresult) == 0:
        print("No Result")

    elif len(myresult) == 1:
        print(myresult)

    cnx.close()

