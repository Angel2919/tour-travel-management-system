import mysql.connector
from mysql.connector import Error

# Establishing connection to MySQL
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="priya@1109##>",
        database="Traveldb"
    )
    if mydb.is_connected():
        mycursor = mydb.cursor()
        print("✅ Connected to MySQL!")
except Error as e:
    print("⚠️ Error while connecting to MySQL:", e)
    mydb = None
    mycursor = None
