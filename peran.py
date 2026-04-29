import streamlit as st
import base64

# Hilangkan sidebar
st.set_page_config(initial_sidebar_state="collapsed")

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
img_base64 = get_base64_image("pages/background.jpg")

#
st.markdown(f"""
<style>

/* ========================
   BACKGROUND IMAGE
   ======================== */
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* hilangkan background default Streamlit */
[data-testid="stAppViewContainer"] > .main {{
    background: transparent;
}}

/* overlay gelap biar teks tetap jelas */
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

/* pastikan konten di atas overlay */
.main {{
    position: relative;
    z-index: 1;
}}

/* Hilangkan sidebar */
[data-testid="stSidebar"] {{
    display: none;
}}

.center-text {{
    text-align: center;
    font-weight: 700;
    color: white;
    text-shadow: 0 2px 8px rgba(0,0,0,0.10);
}}

.center-box {{
    text-align: center;
    font-weight: 700;
    color: white;
    text-shadow: 0 2px 8px rgba(0,0,0,0.10);
}}

/* Tombol */
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
# ========================
# JUDUL
# ========================

st.markdown("<h1 class='center-text'>Sistem Monitoring Status Gizi Balita</h1>", unsafe_allow_html=True)

st.markdown("<h4 class='center-text'>Silakan pilih peran pengguna</h4>", unsafe_allow_html=True)

st.write("---")


# kolom kiri kosong supaya posisi ke tengah
sp1, col1, sp2, col2, sp3 = st.columns([0.7,1,0.5,1,0.7])


# ========================
# ADMIN
# ========================

with col1:

    st.markdown("<div class='center-box'>", unsafe_allow_html=True)

    st.subheader("Admin Posyandu")
    st.write("Kelola data balita")

    if st.button("Masuk sebagai Admin"):
        st.switch_page("pages/loginadmin.py")

    st.markdown("</div>", unsafe_allow_html=True)


# ========================
# ORANG TUA
# ========================

with col2:

    st.markdown("<div class='center-box'>", unsafe_allow_html=True)

    st.subheader("Orang Tua Balita")
    st.write("Cek status gizi anak")

    if st.button("Masuk sebagai Orang Tua"):
        st.switch_page("pages/inputdata.py")

    st.markdown("</div>", unsafe_allow_html=True)
