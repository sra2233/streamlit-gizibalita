import streamlit as st

# Hilangkan sidebar
st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("""
<style>

/* Hilangkan sidebar */
[data-testid="stSidebar"] {display:none;}

/* Judul di tengah */
.center-text {
text-align:center;
}

/* Isi kolom di tengah */
.center-box {
text-align:center;
}

/* Tombol warna hijau */
.stButton>button {
background-color:#28a745;
color:white;
border:none;
border-radius:8px;
padding:10px 20px;
font-weight:bold;
}

.stButton>button:hover {
background-color:#218838;
color:white;
}

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
