import streamlit as st
from koneksi import koneksi_supabase
import base64
supabase = koneksi_supabase()

#
st.set_page_config(initial_sidebar_state="collapsed")

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
    
img_base64 = get_base64_image("pages/background.jpg")

#
st.markdown(f"""
<style>

/* =========================
   BACKGROUND LOGIN ADMIN
   ========================= */
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* overlay gelap hijau army */
[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(27, 46, 36, 0.90);
    z-index: 0;
    pointer-events: none;
}}

/* pastikan konten di atas background */
.main {{
    position: relative;
    z-index: 1;
}}

/* =========================
   CSS PUNYA KAMU (TIDAK DIUBAH)
   ========================= */

/* Hilangkan sidebar */
[data-testid="stSidebar"] {{
    display:none;
}}

.center-text {{
    text-align:center;
    font-weight: 700;
    color: white;
    text-shadow: 0 2px 8px rgba(0,0,0,0.20);
}}

.center-box {{
    text-align: center;
    font-weight: 700;
    color: white;
    text-shadow: 0 2px 8px rgba(0,0,0,0.20);
}}

.stButton > button {{
    background-color: rgba(20, 83, 45, 0.80);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 22px;
    font-weight: 600;
    transition: 0.3s ease;
    box-shadow: 0 2px 6px rgba(0,0,0,0.20);
}}

.stButton > button:hover {{
    background: #111827;
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}}

.stButton > button:active {{
    transform: scale(0.98);
}}

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

col1, col2 = st.columns(2)

with col1:
    login = st.button("Login")

with col2:
    kembali = st.button("Kembali")


# =========================
# PROSES LOGIN
# =========================

if login:

    data = supabase.table("admin").select("*").eq("username", username).eq("password", password).execute()
    
    if data.data:
        st.success("Login berhasil")
        st.switch_page("pages/inputdataadmin.py")

    else:
        st.error("Username atau password salah")


if kembali:
    st.switch_page("peran.py")