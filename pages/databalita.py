import streamlit as st
from koneksi import koneksi_supabase
supabase = koneksi_supabase()
import pandas as pd

# ==========================
# CONFIG
# ==========================

st.set_page_config(
    page_title="Data Balita",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# CSS STYLE
# ==========================

st.markdown("""
<style>

/* Hilangkan menu navigasi bawaan */
[data-testid="stSidebarNav"] {display:none;}

/* Tombol Download */
div.stDownloadButton > button {
    background-color: #1f77ff;
    color: white;
    border-radius: 8px;
}

/* Tombol Hapus */
button[kind="secondary"] {
    background-color: #f39c12;
    color: white;
}

/* Tombol Reset */
button[kind="primary"] {
    background-color: #e74c3c;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# SIDEBAR ADMIN
# ==========================

with st.sidebar:

    st.title("Menu")

    if st.button("Input Data Balita"):
        st.switch_page("pages/inputdataadmin.py")

    if st.button("Data Balita"):
        st.switch_page("pages/databalita.py")

# ==========================
# HALAMAN DATA BALITA
# ==========================

st.title(" Data Balita")

response = supabase.table("balita").select("*").order("id", desc=True).execute()

df = pd.DataFrame(response.data)

st.dataframe(df, use_container_width=True, hide_index=True)

# ==========================
# DOWNLOAD DATA
# ==========================

st.subheader("Download Data")

csv = df.to_csv(index=False)

st.download_button(
    "Download Data",
    csv,
    "data_balita.csv",
    "text/csv"
)

# ==========================
# HAPUS DATA
# ==========================

st.subheader("Hapus Data Balita")

if not df.empty:

    pilih_id = st.selectbox(
        "Pilih ID Data yang akan dihapus",
        df["id"]
    )

    if st.button("Hapus Data", type="secondary"):

        supabase.table("balita").delete().eq("id", pilih_id).execute()

        st.success("Data berhasil dihapus")

        st.rerun()

# ==========================
# RESET DATA
# ==========================

st.subheader("Reset Semua Data")

konfirmasi = st.checkbox("Saya yakin ingin menghapus semua data")

col1, col2 = st.columns(2)

with col1:

    if st.button("Reset Data Balita", type="primary"):

        if konfirmasi:

            supabase.table("balita").delete().neq("id", 0).execute()

            st.success("Semua data berhasil dihapus dan ID kembali ke 1")

            st.rerun()

        else:
            st.warning("Centang konfirmasi terlebih dahulu")

# ==========================
# TOMBOL KELUAR
# ==========================

with col2:

    if st.button("Keluar"):
        st.switch_page("peran.py")