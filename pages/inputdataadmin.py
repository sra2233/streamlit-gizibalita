import streamlit as st
from koneksi import koneksi_supabase
import pandas as pd
import math
import base64
supabase = koneksi_supabase()

# ==========================
# CONFIG
# ==========================

st.set_page_config(initial_sidebar_state="expanded")

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

/* overlay hijau army  */
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

/* konten di atas */
.main {{
    position: relative;
    z-index: 1;
}}

/* ========================
   SIDEBAR
   ======================== */
[data-testid="stSidebarNav"] {{
    display:none;
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
   TOMBOL
   ======================== */
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
}}

.stButton > button:active {{
    transform: scale(0.98);
}}

</style>
""", unsafe_allow_html=True)

# ====================
# SIDEBAR ADMIN
# ====================

with st.sidebar:

    st.title("Menu")

    if st.button("Input Data Balita"):
        st.switch_page("pages/inputdataadmin.py")

    if st.button("Data Balita"):
        st.switch_page("pages/databalita.py")
    
    st.markdown("---")  # \

    if st.button("Keluar"):
        st.switch_page("peran.py")

#
st.title("Input Data Balita")

# ======================
# DATA WHO 
# ======================

data_who = {

("Perempuan",0):{"L":0.3809,"M":3.2322,"S":0.14171},
("Perempuan",1):{"L":0.1714,"M":4.1873,"S":0.13724},
("Perempuan",2):{"L":0.0962,"M":5.1282,"S":0.13000},
("Perempuan",3):{"L":0.0402,"M":5.8458,"S":0.12619},
("Perempuan",4):{"L":-0.0050,"M":6.4237,"S":0.12402},
("Perempuan",5):{"L":-0.0430,"M":6.8985,"S":0.12274},
("Perempuan",6):{"L":-0.0756,"M":7.2970,"S":0.12204},
("Perempuan",7):{"L":-0.1039,"M":7.6422,"S":0.12178},
("Perempuan",8):{"L":-0.1288,"M":7.9487,"S":0.12181},
("Perempuan",9):{"L":-0.1507,"M":8.2254,"S":0.12199},
("Perempuan",10):{"L":-0.1700,"M":8.4800,"S":0.12223},
("Perempuan",11):{"L":-0.1872,"M":8.7192,"S":0.12247},
("Perempuan",12):{"L":-0.2024,"M":8.9481,"S":0.12268},
("Perempuan",13):{"L":-0.2158,"M":9.1699,"S":0.12283},
("Perempuan",14):{"L":-0.2278,"M":9.3870,"S":0.12294},
("Perempuan",15):{"L":-0.2384,"M":9.6008,"S":0.12299},
("Perempuan",16):{"L":-0.2478,"M":9.8124,"S":0.12303},
("Perempuan",17):{"L":-0.2562,"M":10.0226,"S":0.12306},
("Perempuan",18):{"L":-0.2637,"M":10.2315,"S":0.12309},
("Perempuan",19):{"L":-0.2703,"M":10.4393,"S":0.12315},
("Perempuan",20):{"L":-0.2762,"M":10.6464,"S":0.12323},
("Perempuan",21):{"L":-0.2815,"M":10.8534,"S":0.12335},
("Perempuan",22):{"L":-0.2862,"M":11.0608,"S":0.12350},
("Perempuan",23):{"L":-0.2903,"M":11.2688,"S":0.12369},
("Perempuan",24):{"L":-0.2941,"M":11.4775,"S":0.12390},
("Perempuan",25):{"L":-0.2975,"M":11.6864,"S":0.12414},
("Perempuan",26):{"L":-0.3005,"M":11.8947,"S":0.12441},
("Perempuan",27):{"L":-0.3032,"M":12.1015,"S":0.12472},
("Perempuan",28):{"L":-0.3057,"M":12.3059,"S":0.12506},
("Perempuan",29):{"L":-0.3079,"M":12.5082,"S":0.12543},
("Perempuan",30):{"L":-0.3099,"M":12.7086,"S":0.12582},
("Perempuan",31):{"L":-0.3118,"M":12.9075,"S":0.12624},
("Perempuan",32):{"L":-0.3135,"M":13.1052,"S":0.12669},
("Perempuan",33):{"L":-0.3151,"M":13.3019,"S":0.12716},
("Perempuan",34):{"L":-0.3166,"M":13.4979,"S":0.12766},
("Perempuan",35):{"L":-0.3180,"M":13.6934,"S":0.12819},
("Perempuan",36):{"L":-0.3193,"M":13.8886,"S":0.12874},
("Perempuan",37):{"L":-0.3205,"M":14.0836,"S":0.12931},
("Perempuan",38):{"L":-0.3217,"M":14.2785,"S":0.12992},
("Perempuan",39):{"L":-0.3228,"M":14.4735,"S":0.13055},
("Perempuan",40):{"L":-0.3238,"M":14.6686,"S":0.13121},
("Perempuan",41):{"L":-0.3248,"M":14.8639,"S":0.13190},
("Perempuan",42):{"L":-0.3257,"M":15.0595,"S":0.13261},
("Perempuan",43):{"L":-0.3266,"M":15.2555,"S":0.13335},
("Perempuan",44):{"L":-0.3275,"M":15.4518,"S":0.13412},
("Perempuan",45):{"L":-0.3283,"M":15.6486,"S":0.13491},
("Perempuan",46):{"L":-0.3291,"M":15.8458,"S":0.13573},
("Perempuan",47):{"L":-0.3299,"M":16.0435,"S":0.13658},
("Perempuan",48):{"L":-0.3307,"M":16.2416,"S":0.13745},
("Perempuan",49):{"L":-0.3314,"M":16.4402,"S":0.13835},
("Perempuan",50):{"L":-0.3321,"M":16.6393,"S":0.13927},
("Perempuan",51):{"L":-0.3328,"M":16.8388,"S":0.14022},
("Perempuan",52):{"L":-0.3335,"M":17.0388,"S":0.14119},
("Perempuan",53):{"L":-0.3342,"M":17.2392,"S":0.14218},
("Perempuan",54):{"L":-0.3348,"M":17.4400,"S":0.14320},
("Perempuan",55):{"L":-0.3355,"M":17.6413,"S":0.14424},
("Perempuan",56):{"L":-0.3466,"M":17.5136,"S":0.14525},
("Perempuan",57):{"L":-0.3479,"M":17.6916,"S":0.14600},
("Perempuan",58):{"L":-0.3492,"M":17.8686,"S":0.14675},
("Perempuan",59):{"L":-0.3505,"M":18.0445,"S":0.14748},
("Perempuan",60):{"L":-0.3518,"M":18.2193,"S":0.14821},


("Laki-laki",0):{"L":0.3487,"M":3.3464,"S":0.14602},
("Laki-laki",1):{"L":0.2297,"M":4.4709,"S":0.13395},
("Laki-laki",2):{"L":0.1970,"M":5.5675,"S":0.12385},
("Laki-laki",3):{"L":0.1738,"M":6.3762,"S":0.11727},
("Laki-laki",4):{"L":0.1553,"M":7.0023,"S":0.11316},
("Laki-laki",5):{"L":0.1395,"M":7.5105,"S":0.11080},
("Laki-laki",6):{"L":0.1257,"M":7.9340,"S":0.10958},
("Laki-laki",7):{"L":0.1134,"M":8.2970,"S":0.10902},
("Laki-laki",8):{"L":0.1021,"M":8.6151,"S":0.10882},
("Laki-laki",9):{"L":0.0917,"M":8.9014,"S":0.10881},
("Laki-laki",10):{"L":0.0820,"M":9.1649,"S":0.10891},
("Laki-laki",11):{"L":0.0730,"M":9.4122,"S":0.10906},
("Laki-laki",12):{"L":0.0644,"M":9.6479,"S":0.10925},
("Laki-laki",13):{"L":0.0563,"M":9.8749,"S":0.10949},
("Laki-laki",14):{"L":0.0487,"M":10.0953,"S":0.10976},
("Laki-laki",15):{"L":0.0413,"M":10.3108,"S":0.11007},
("Laki-laki",16):{"L":0.0343,"M":10.5228,"S":0.11041},
("Laki-laki",17):{"L":0.0275,"M":10.7319,"S":0.11079},
("Laki-laki",18):{"L":0.0211,"M":10.9385,"S":0.11119},
("Laki-laki",19):{"L":0.0148,"M":11.1430,"S":0.11164},
("Laki-laki",20):{"L":0.0087,"M":11.3462,"S":0.11211},
("Laki-laki",21):{"L":0.0029,"M":11.5486,"S":0.11261},
("Laki-laki",22):{"L":-0.0028,"M":11.7504,"S":0.11314},
("Laki-laki",23):{"L":-0.0083,"M":11.9514,"S":0.11369},
("Laki-laki",24):{"L":-0.0137,"M":12.1515,"S":0.11426},
("Laki-laki",25):{"L":-0.0189,"M":12.3502,"S":0.11485},
("Laki-laki",26):{"L":-0.0240,"M":12.5466,"S":0.11544},
("Laki-laki",27):{"L":-0.0289,"M":12.7401,"S":0.11604},
("Laki-laki",28):{"L":-0.0337,"M":12.9303,"S":0.11664},
("Laki-laki",29):{"L":-0.0385,"M":13.1169,"S":0.11723},
("Laki-laki",30):{"L":-0.0431,"M":13.3000,"S":0.11781},
("Laki-laki",31):{"L":-0.0476,"M":13.4798,"S":0.11839},
("Laki-laki",32):{"L":-0.0520,"M":13.6567,"S":0.11896},
("Laki-laki",33):{"L":-0.0564,"M":13.8309,"S":0.11953},
("Laki-laki",34):{"L":-0.0606,"M":14.0031,"S":0.12008},
("Laki-laki",35):{"L":-0.0648,"M":14.1736,"S":0.12062},
("Laki-laki",36):{"L":-0.0689,"M":14.3429,"S":0.12116},
("Laki-laki",37):{"L":-0.0729,"M":14.5113,"S":0.12168},
("Laki-laki",38):{"L":-0.0769,"M":14.6791,"S":0.12220},
("Laki-laki",39):{"L":-0.0808,"M":14.8466,"S":0.12271},
("Laki-laki",40):{"L":-0.0846,"M":15.0140,"S":0.12322},
("Laki-laki",41):{"L":-0.0883,"M":15.1813,"S":0.12373},
("Laki-laki",42):{"L":-0.0920,"M":15.3486,"S":0.12425},
("Laki-laki",43):{"L":-0.0957,"M":15.5158,"S":0.12478},
("Laki-laki",44):{"L":-0.0993,"M":15.6828,"S":0.12531},
("Laki-laki",45):{"L":-0.1028,"M":15.8497,"S":0.12586},
("Laki-laki",46):{"L":-0.1063,"M":16.0163,"S":0.12643},
("Laki-laki",47):{"L":-0.1097,"M":16.1827,"S":0.12700},
("Laki-laki",48):{"L":-0.1131,"M":16.3489,"S":0.12759},
("Laki-laki",49):{"L":-0.1165,"M":16.5150,"S":0.12819},
("Laki-laki",50):{"L":-0.1198,"M":16.6811,"S":0.12880},
("Laki-laki",51):{"L":-0.1230,"M":16.8471,"S":0.12943},
("Laki-laki",52):{"L":-0.1262,"M":17.0132,"S":0.13005},
("Laki-laki",53):{"L":-0.1294,"M":17.1792,"S":0.13069},
("Laki-laki",54):{"L":-0.1325,"M":17.3452,"S":0.13133},
("Laki-laki",55):{"L":-0.1356,"M":17.5111,"S":0.13197},
("Laki-laki",56):{"L":-0.1387,"M":17.6768,"S":0.13261},
("Laki-laki",57):{"L":-0.1417,"M":17.8422,"S":0.13325},
("Laki-laki",58):{"L":-0.1447,"M":18.0073,"S":0.13389},
("Laki-laki",59):{"L":-0.1477,"M":18.1722,"S":0.13453},
("Laki-laki",60):{"L":-0.1506,"M":18.3366,"S":0.13517}
}

# ======================
# FUNGSI HITUNG Z SCORE
# ======================

def hitung_zscore(berat, jk, usia):

    data = data_who.get((jk, usia))

    if data is None:
        return None

    L = data["L"]
    M = data["M"]
    S = data["S"]

    if L == 0:
        z = math.log(berat / M) / S
    else:
        z = ((berat / M)**L - 1) / (L * S)

    if z > 3:
        z = 3
    elif z < -3:
        z = -3

    return round(z, 2)


# ======================
# STATUS GIZI
# ======================

def status_gizi(z):

    if z < -3:
        return "Gizi Buruk"
    elif z < -2:
        return "Gizi Kurang"
    elif z <= 2:
        return "Gizi Normal"
    else:
        return "Gizi Lebih"

# ======================
# FUNGSI K-MEANS
# ======================

def hitung_kmeans(usia, berat):

    # centroid
    c1 = (53.63636364, 14.85454545)
    c2 = (29.55, 10.27)
    c3 = (11.29411765, 8.144117647)

    # hitung jarak
    d1 = math.sqrt((usia - c1[0])**2 + (berat - c1[1])**2)
    d2 = math.sqrt((usia - c2[0])**2 + (berat - c2[1])**2)
    d3 = math.sqrt((usia - c3[0])**2 + (berat - c3[1])**2)

    jarak = [d1, d2, d3]
    min_jarak = min(jarak)

    # tentukan cluster + kategori
    if min_jarak == d1:
        cluster = 1
        kategori = "Usia Tinggi"
    elif min_jarak == d2:
        cluster = 2
        kategori = "Usia Sedang"
    else:
        cluster = 3
        kategori = "Usia Rendah"

    #  RETURN HARUS DI DALAM FUNCTION
    return round(d1,2), round(d2,2), round(d3,2), cluster

# ======================
# FORM INPUT
# ======================

nama = st.text_input("Nama Anak")

jk = st.selectbox(
"Jenis Kelamin",
["Perempuan","Laki-laki"]
)

usia = st.number_input(
"Usia (bulan)",
0,
60
)

berat = st.number_input(
"Berat Badan (kg)",
0.0
)

if berat <= 0:
    st.warning("Berat badan harus lebih dari 0")

# ======================
# HITUNG
# ======================

if st.button("Hitung", type="secondary"):

    z = hitung_zscore(berat, jk, usia)

    if z is None:
        st.error("Data WHO tidak ditemukan untuk usia tersebut")
    else:
        status = status_gizi(z)

        # 🔥 K-MEANS
        d1, d2, d3, cluster, = hitung_kmeans(usia, berat)

        # simpan session
        st.session_state.z = z
        st.session_state.status = status
        st.session_state.d1 = d1
        st.session_state.d2 = d2
        st.session_state.d3 = d3
        st.session_state.cluster = cluster

        # hasil lengkap
        st.session_state.hasil = pd.DataFrame([{
            "Nama": nama,
            "Jenis Kelamin": jk,
            "Usia (Bulan)": usia,
            "Berat Badan": berat,
            "Jarak C1": d1,
            "Jarak C2": d2,
            "Jarak C3": d3,
            "Cluster": cluster,
            "Z-Score": z,
            "Status": status
        }])


# ======================
# TAMPILKAN HASIL
# ======================
if "hasil" in st.session_state:
    st.markdown(
        "<h2 style='text-align:center;'>Hasil Perhitungan</h2>",
        unsafe_allow_html=True
    )

    st.dataframe(
        st.session_state.hasil,
        hide_index=True,
        use_container_width=True
    )


# ======================
# TOMBOL SIMPAN
# ======================
col1, col2 = st.columns(2)

with col1:
       if st.button("Simpan Data", type="primary", key="btn_simpan"):

        try:
            supabase.table("balita").insert({
                "nama": nama,
                "jenis_kelamin": jk,
                "usia": usia,
                "berat": berat,
                "zscore": st.session_state.z,
                "status": st.session_state.status,
                "c1": st.session_state.d1,
                "c2": st.session_state.d2,
                "c3": st.session_state.d3,
                "cluster": st.session_state.cluster
            }).execute()

            st.success("Data berhasil disimpan")

            st.switch_page("pages/databalita.py")

        except Exception as e:
            st.error(f"Gagal menyimpan data: {e}")

with col2:
    if st.button("Hapus"):

        keys_to_remove = ["z", "status", "hasil"]

        for key in keys_to_remove:
            st.session_state.pop(key, None)

    
# ======================
# UPLOAD EXCEL / CSV
# ======================

st.write("---")

st.subheader("Upload Data Excel / CSV")

file = st.file_uploader(
"Upload file",
type=["csv","xlsx"]
)

if file:

    # baca file
    if file.name.endswith("csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    # ubah nama kolom menjadi huruf kecil
    df.columns = df.columns.str.lower().str.strip()

    # samakan nama kolom
    df = df.rename(columns={

        # nama
        "nama": "nama",
        "nama anak": "nama",
        "nama balita": "nama",
        "nama_anak": "nama",
        "NAMA": "nama",
        "NAMA_ANAK":"nama",

        # jenis kelamin
        "jenis_kelamin": "jenis_kelamin",
        "jenis kelamin": "jenis_kelamin",
        "jk": "jenis_kelamin",
        "JENIS KELAMIN":"jenis_kelamin",
        "JENIS_KELAMIN":"jenis_kelamin",

        # usia
        "usia": "usia",
        "umur": "usia",
        "usia (bulan)": "usia",
        "USIA": "usia",
        "usia_anak": "usia",
        "USIA_ANAK": "usia",

        # berat
        "berat": "berat",
        "berat badan": "berat",
        "bb": "berat",
        "berat_badan": "berat",
        "BERAT":"berat",
        "BB": "berat",
        "bb_anak": "berat"


    })

    # bersihkan isi data
    df["nama"] = df["nama"].astype(str).str.strip()

    df["jenis_kelamin"] = df["jenis_kelamin"].astype(str).str.strip().str.lower()

    df["jenis_kelamin"] = df["jenis_kelamin"].replace({
        "laki laki": "Laki-laki",
        "laki-laki": "Laki-laki",
        "lakilaki": "Laki-laki",
        "perempuan": "Perempuan"
    })

    df["usia"] = pd.to_numeric(df["usia"], errors="coerce")
    df["berat"] = pd.to_numeric(df["berat"], errors="coerce")

    # hapus data kosong
    df = df.dropna(subset=["nama","jenis_kelamin","usia","berat"])

    st.dataframe(df)

    if st.button("Simpan Semua Data"):

        for i, row in df.iterrows():

            z = hitung_zscore(
                row["berat"],
                row["jenis_kelamin"],
                int(row["usia"])
            )

            if z is None:
                continue

            status = status_gizi(z)

            d1, d2, d3, cluster = hitung_kmeans(
                int(row["usia"]),
                row["berat"]
            )

            supabase.table("balita").insert({
                "nama": row["nama"],
                "jenis_kelamin": row["jenis_kelamin"],
                "usia": int(row["usia"]),
                "berat": row["berat"],
                "zscore": z,
                "status": status,
                "c1": d1,
                "c2": d2,
                "c3": d3,
                "cluster": cluster
            }).execute()

        st.success("Semua data berhasil disimpan")
        st.switch_page("pages/databalita.py")
