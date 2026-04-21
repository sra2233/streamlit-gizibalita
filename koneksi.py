import mysql.connector
import streamlit as st

def koneksi_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="posyandu"
    )
    return conn
