import mysql.connector
DATABASE = mysql.connector.connect(
    host="localhost",
    user="Sohail",
    password="Sohail123"
)

cursor = DATABASE.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS customer_management_db")


print("Database created successfully")