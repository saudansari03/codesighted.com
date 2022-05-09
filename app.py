import mysql.connector
mydb  = mysql.connector.connect(host = 'localhost', user = 'root', password = '9970653041',database = 'essel_world')
mycursor = mydb.cursor()
mycursor.execute("show databases")
for x in mycursor:
    print(x)



