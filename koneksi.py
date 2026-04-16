import mysql.connector

def koneksi_db():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="posyandu"
    )

    return conn