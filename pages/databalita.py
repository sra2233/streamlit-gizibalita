import streamlit as st
from koneksi import koneksi_supabase
supabase = koneksi_supabase()
import base64
import pandas as pd
import plotly.graph_objects as go
from io import BytesIO
# ==========================
# CONFIG
# ==========================

st.set_page_config(page_title="Data Balita",layout="wide",initial_sidebar_state="expanded")

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
img_base64 = get_base64_image("pages/background.jpg")

# ==========================
# CSS STYLE
# ==========================
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

/* overlay hijau army */
[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(27, 46, 36, 0.90);
    z-index: 0;
    pointer-events: none;
}}

/* konten di atas */
.main {{
    position: relative;
    z-index: 1;
}}

/* ========================
   SIDEBAR NAV
   ======================== */
[data-testid="stSidebarNav"] {{
    display: none;
}}

/* ========================
   TEXT
   ======================== */
h1 {{
    text-align: center;
    color: white;
    font-weight: 800;
    text-shadow: 0 2px 10px rgba(0,0,0,0.5);
}}

label {{
    color: white !important;
    font-weight: 600;
}}

/* ========================
   SEMUA TOMBOL (SATU WARNA)
   ======================== */
.stButton > button,
div.stDownloadButton > button {{
    background-color: rgba(20, 83, 45, 0.85);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 22px;
    font-weight: 600;
    transition: 0.3s ease;
    box-shadow: 0 2px 6px rgba(0,0,0,0.25);
}}

.stButton > button:hover,
div.stDownloadButton > button:hover {{
    background: #111827;
    transform: translateY(-2px);
}}

.stButton > button:active {{
    transform: scale(0.98);
}}

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

    st.markdown("---")  # garis pemisah

    if st.button("Keluar"):
        st.switch_page("peran.py")

# ==========================
# HALAMAN DATA BALITA
# ==========================

st.title(" Data Balita")

response = supabase.table("balita").select("*").order("id", desc=False).execute()

df = pd.DataFrame(response.data)
df = df.rename(columns={
    "id": "ID",
    "nama": "Nama",
    "jenis_kelamin": "Jenis Kelamin",
    "usia": "Usia (Bulan)",
    "berat": "Berat Badan (Kg)",
    "c1": "Jarak C1",
    "c2": "Jarak C2",
    "c3": "Jarak C3",
    "cluster": "Cluster",
    "zscore": "Nilai Z-Score",
    "status": "Status Gizi"
})

st.dataframe(df, use_container_width=True, hide_index=True)

# ==========================
# DIAGRAM DATA
# ==========================
st.subheader("Visualisasi Z-Score per Anak")

if not df.empty:

    df_sorted = df.sort_values(by="ID")

    # warna manual (TIDAK bikin grouping)
    colors = []
    for s in df_sorted["Status Gizi"]:
        if s == "Gizi Kurang":
            colors.append("#B22222")
        elif s == "Gizi Normal":
            colors.append("#0B3D91")
        elif s == "Gizi Lebih":
            colors.append("#2F4F2F")
        elif s == "Gizi Buruk":
            colors.append("#5A0000")
        else:
            colors.append("gray")

    fig = go.Figure()

    fig.add_bar(
    x=df_sorted["Nama"],
    y=df_sorted["Nilai Z-Score"],
    marker_color=colors,
    width=0.4,
    hovertext="Nama: " + df_sorted["Nama"] +
          "<br>Status Gizi: " + df_sorted["Status Gizi"] +
          "<br>Cluster: " + df_sorted["Cluster"].astype(str) +
          "<br>Z-Score: " + df_sorted["Nilai Z-Score"].astype(str),
    hoverinfo="text"
)

#
fig.update_traces(
    text=df_sorted["Nama"],
    textposition="outside",
    textfont=dict(size=8)
)

# 
fig.update_layout(
    height=450,
    width=len(df_sorted) * 60,
    xaxis_tickangle=-90,
    xaxis=dict(tickfont=dict(size=10))
)

st.plotly_chart(
    fig,
    use_container_width=False,  
    config={"scrollZoom": True}
)
# ==========================
# DOWNLOAD DATA
# ==========================

st.subheader("Download Data")

output = BytesIO()
df.to_excel(output, index=False, engine='openpyxl')

st.download_button(
    "Download Data Excel",
    data=output.getvalue(),
    file_name="data_balita.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# ==========================
# HAPUS DATA
# ==========================

st.subheader("Hapus Data Balita")

if not df.empty:

    pilih_id = st.selectbox(
        "Pilih ID Data yang akan dihapus",
        df["ID"]
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

if st.button("Reset Data Balita", type="primary"):

    if konfirmasi:

        supabase.table("balita").delete().neq("id", 0).execute()

        st.success("Semua data berhasil dihapus dan ID kembali ke 1")

        st.rerun()

    else:
        st.warning("Centang konfirmasi terlebih dahulu")