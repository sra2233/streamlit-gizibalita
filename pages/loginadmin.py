import streamlit as st
from koneksi import koneksi_db

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("""
<style>

/* Hilangkan sidebar */
[data-testid="stSidebar"] {display:none;}

/* Judul di tengah */
.center-text {
text-align:center;
}

/* Tombol LOGIN (biru) */
div.stButton > button:first-child {
background-color:#007BFF;
color:white;
border:none;
border-radius:8px;
padding:10px 20px;
font-weight:bold;
}

/* Hover login */
div.stButton > button:first-child:hover {
background-color:#0069d9;
color:white;
}

/* Tombol KEMBALI (merah) */
div.stButton:nth-of-type(2) button {
background-color:#dc3545;
color:white;
border:none;
border-radius:8px;
padding:10px 20px;
font-weight:bold;
}

/* Hover kembali */
div.stButton:nth-of-type(2) button:hover {
background-color:#c82333;
color:white;
}

</style>
""", unsafe_allow_html=True)


# =========================
# JUDUL
# =========================

st.markdown("<h2 class='center-text'>Login Admin Posyandu</h2>", unsafe_allow_html=True)

st.write("")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

st.write("")

# =========================
# TOMBOL
# =========================

col1, col2, col3 = st.columns([1,2,1])

with col1:
    login = st.button("Login")

with col3:
    kembali = st.button("Kembali")


# =========================
# PROSES LOGIN
# =========================

if login:

    conn = koneksi_db()
    cursor = conn.cursor()

    query = "SELECT * FROM admin WHERE username=%s AND password=%s"
    cursor.execute(query,(username,password))

    data = cursor.fetchone()

    if data:
        st.success("Login berhasil")
        st.switch_page("pages/inputdataadmin.py")

    else:
        st.error("Username atau password salah")


if kembali:
    st.switch_page("peran.py")
