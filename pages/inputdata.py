import streamlit as st
import math
import pandas as pd
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

/* =========================
   BACKGROUND LOGIN
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
    background: rgba(27, 46, 36, 0.85);  /* sedikit lebih enak dari 0.90 */
    z-index: 0;
    pointer-events: none;
}}

/* konten di atas background */
.main {{
    position: relative;
    z-index: 1;
}}

/* =========================
   SIDEBAR
   ========================= */
[data-testid="stSidebar"] {{
    display:none;
}}

/* =========================
   TEKS CENTER
   ========================= */

/* judul utama Streamlit */
h1 {{
    text-align: center;
    color: white;
    font-weight: 800;
    text-shadow: 0 2px 10px rgba(0,0,0,0.6);
}}

/* subjudul / teks biasa */
h2, h3, h4, p {{
    text-align: center;
    color: white;
    font-weight: 600;
    text-shadow: 0 2px 8px rgba(0,0,0,0.5);
}}

.center-text {{
    text-align:center;
    font-weight: 700;
    color: white;
    text-shadow: 0 2px 8px rgba(0,0,0,0.5);
}}

.center-box {{
    text-align:center;
    font-weight: 700;
    color: white;
    text-shadow: 0 2px 8px rgba(0,0,0,0.5);
}}

label {{
    font-size: 20px !important;
    font-weight: 700 !important;
    color: white !important;
    text-shadow: 0 2px 6px rgba(0,0,0,0.4);
}}

/* =========================
   BUTTON
   ========================= */
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

st.title("Cek Status Gizi Balita")


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
("Perempuan",29):{"L":-0.3080,"M":12.5073,"S":0.12545},
("Perempuan",30):{"L":-0.3101,"M":12.7055,"S":0.12587},
("Perempuan",31):{"L":-0.3120,"M":12.9006,"S":0.12633},
("Perempuan",32):{"L":-0.3138,"M":13.0930,"S":0.12683},
("Perempuan",33):{"L":-0.3155,"M":13.2837,"S":0.12737},
("Perempuan",34):{"L":-0.3171,"M":13.4731,"S":0.12794},
("Perempuan",35):{"L":-0.3186,"M":13.6618,"S":0.12855},
("Perempuan",36):{"L":-0.3201,"M":13.8503,"S":0.12919},
("Perempuan",37):{"L":-0.3216,"M":14.0385,"S":0.12988},
("Perempuan",38):{"L":-0.3230,"M":14.2265,"S":0.13059},
("Perempuan",39):{"L":-0.3243,"M":14.4140,"S":0.13135},
("Perempuan",40):{"L":-0.3257,"M":14.6010,"S":0.13213},
("Perempuan",41):{"L":-0.3270,"M":14.7873,"S":0.13293},
("Perempuan",42):{"L":-0.3283,"M":14.9727,"S":0.13376},
("Perempuan",43):{"L":-0.3296,"M":15.1573,"S":0.13460},
("Perempuan",44):{"L":-0.3309,"M":15.3410,"S":0.13545},
("Perempuan",45):{"L":-0.3322,"M":15.5240,"S":0.13630},
("Perempuan",46):{"L":-0.3335,"M":15.7064,"S":0.13716},
("Perempuan",47):{"L":-0.3348,"M":15.8882,"S":0.13800},
("Perempuan",48):{"L":-0.3361,"M":16.0697,"S":0.13884},
("Perempuan",49):{"L":-0.3374,"M":16.2511,"S":0.13968},
("Perempuan",50):{"L":-0.3387,"M":16.4322,"S":0.14051},
("Perempuan",51):{"L":-0.3400,"M":16.6133,"S":0.14132},
("Perempuan",52):{"L":-0.3414,"M":16.7942,"S":0.14213},
("Perempuan",53):{"L":-0.3427,"M":16.9748,"S":0.14293},
("Perempuan",54):{"L":-0.3440,"M":17.1551,"S":0.14371},
("Perempuan",55):{"L":-0.3453,"M":17.3347,"S":0.14448},
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
    
#
def hitung_kmeans(usia, berat):

    # centroid (ambil dari hasil admin kamu)
    c1 = (53.63636364, 14.85454545)
    c2 = (29.55, 10.27)
    c3 = (11.29411765, 8.144117647)

    # hitung jarak
    d1 = math.sqrt((usia - c1[0])**2 + (berat - c1[1])**2)
    d2 = math.sqrt((usia - c2[0])**2 + (berat - c2[1])**2)
    d3 = math.sqrt((usia - c3[0])**2 + (berat - c3[1])**2)

    # tentukan cluster
    if usia <= 20:
        cluster = 3
        kategori = "Usia Rendah"
    elif usia <= 40:
        cluster = 2
        kategori = "Usia Sedang"
    else:
        cluster = 1
        kategori = "Usia Tinggi"

    return cluster

# ======================
# INPUT DATA
# ======================

st.subheader("Input Data Anak")

nama = st.text_input("Nama Anak")
jk = st.selectbox("Jenis Kelamin",["Perempuan","Laki-laki"])
usia = st.number_input("Usia (bulan)",0,60)
berat = st.number_input("Berat Badan (kg)",0.0)


# ======================
# HITUNG STATUS GIZI
# ======================

if st.button("Hitung", type="primary"):

    z = hitung_zscore(berat, jk, usia)

    if z is None:
        st.error("Data WHO tidak ditemukan")
    else:
        status = status_gizi(z)

        # K-MEANS
        cluster = hitung_kmeans(usia, berat)

        # simpan session
        st.session_state.nama = nama
        st.session_state.jk = jk
        st.session_state.usia = usia
        st.session_state.berat = berat
        st.session_state.z = z
        st.session_state.status = status
        st.session_state.cluster = cluster

        # hasil 
        st.session_state.hasil = pd.DataFrame([{
            "Nama": nama,
            "Jenis Kelamin": jk,
            "Usia (bulan)": usia,
            "Berat Badan (kg)": berat,
            "Z-Score": z,
            "Status Gizi": status,
            "Cluster": cluster
        }])

# ======================
# TAMPILKAN HASIL
# ======================

if all(key in st.session_state for key in ["nama","jk","usia","berat","z","status","cluster"]):

    st.markdown("<h3 style='text-align:center;'>Hasil Perhitungan</h3>", unsafe_allow_html=True)

    data_hasil = pd.DataFrame([{
        "Nama": st.session_state.nama,
        "Jenis Kelamin": st.session_state.jk,
        "Usia (bulan)": st.session_state.usia,
        "Berat Badan (kg)": st.session_state.berat,
        "Z Score": round(st.session_state.z, 2),
        "Status Gizi": st.session_state.status,
        "Cluster": st.session_state.cluster 
    }])
    
    # tampilkan tabel tanpa nomor
    st.dataframe(data_hasil, hide_index=True, use_container_width=True)

    # ======================
    # KETERANGAN HASIL
    # ======================

    st.markdown("### Keterangan")

    cluster = st.session_state.cluster
    status = st.session_state.status

    # mapping penjelasan cluster
    if cluster == 1:
        keterangan_cluster = "Cluster 1: Anak usia 41–60 bulan (kelompok usia tinggi)"
    elif cluster == 2:
        keterangan_cluster = "Cluster 2: Anak usia 21–40 bulan (kelompok usia sedang)"
    else:
        keterangan_cluster = "Cluster 3: Anak usia 0–20 bulan (kelompok usia rendah)"

    # tampilkan keterangan utama
    st.markdown(f"""
    - **{keterangan_cluster}**
    - Berdasarkan perhitungan Z-Score, status gizi anak termasuk **{status}**
    """)

    # ======================
    # SARAN / EDUKASI
    # ======================

    st.markdown("### Saran")

    st.markdown("""
    Untuk mendapatkan penanganan yang lebih tepat, disarankan:

    - Melakukan konsultasi dengan petugas **Posyandu**
    - Berkonsultasi dengan **Bidan atau Tenaga Kesehatan**
    - Memantau pertumbuhan anak secara rutin setiap bulan
    - Memberikan asupan gizi yang seimbang sesuai usia anak

    Jika terdapat kondisi gizi kurang atau gizi buruk, segera lakukan pemeriksaan lanjutan ke fasilitas kesehatan terdekat.
    """)

    # ======================
    # HAPUS HASIL
    # ======================

    if st.button("Hapus Hasil",key="hapus"):

        del st.session_state.z
        del st.session_state.status
        del st.session_state.nama
        del st.session_state.jk
        del st.session_state.usia
        del st.session_state.berat
        del st.session_state.cluster
         
        st.rerun()


# ======================
# LOGOUT
# ======================

st.write("---")

if st.button("Keluar", key="keluar"):

    st.switch_page("peran.py")