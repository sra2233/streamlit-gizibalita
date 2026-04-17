import mysql.connector
import streamlit as st

def koneksi_db():
    conn = mysql.connector.connect(
        host=st.secrets["mysql.railway.internal"],
        user=st.secrets["root"],
        password=st.secrets["KIUEBrtOGqRgYIYstrlIWnKLvCacStYh"],
        database=st.secrets["railway"],
        port=int(st.secrets["MYSQLPORT"])
    )
    return conn
