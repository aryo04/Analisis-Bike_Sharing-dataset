import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("main_data.csv")

# Mapping Musim & Cuaca jika diperlukan
season_mapping = {
    "Musim Semi": "Spring",
    "Musim Panas": "Summer",
    "Musim Gugur": "Fall",
    "Musim Dingin": "Winter"
}
weather_mapping = {
    "Cerah": "Clear",
    "Berawan": "Cloudy",
    "Hujan": "Rainy",
    "Badai": "Storm"
}

df["season"] = df["season"].map(season_mapping)
df["weathersit"] = df["weathersit"].map(weather_mapping)

# Title
st.title("🚴‍♂️ Bike Sharing Dashboard")

# Create tabs
tab1, tab2 = st.tabs(["📊 Tren Peminjaman", "⏳ Jam Puncak Peminjaman"])

with tab1:
    st.subheader("Bagaimana tren peminjaman sepeda berdasarkan musim dan kondisi cuaca?")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=df, x="season", y="cnt", hue="weathersit", ci=None, ax=ax)
    ax.set_title("Jumlah Peminjaman Sepeda Berdasarkan Musim dan Cuaca")
    ax.set_xlabel("Musim")
    ax.set_ylabel("Jumlah Peminjaman")
    ax.legend(title="Kondisi Cuaca")
    
    st.pyplot(fig)  # Menampilkan grafik dengan benar
    
    st.markdown("""
    **📌 Kesimpulan**:
    - Musim gugur memiliki jumlah peminjaman tertinggi, sedangkan musim semi memiliki jumlah peminjaman terendah.
    - Cuaca cerah menjadi kondisi paling ideal untuk peminjaman sepeda, sementara saat hujan ringan atau berawan, jumlah peminjaman cenderung lebih rendah. Hal ini menunjukkan bahwa musim dan cuaca sangat berpengaruh terhadap jumlah peminjaman sepeda.
    """)

with tab2:
    st.subheader("Pada jam berapa peminjaman sepeda mencapai puncaknya dalam sehari?")
    
    if "hr" in df.columns and df["hr"].notna().sum() > 0:
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(x="hr", y="cnt", data=df, estimator="sum", ci=None, 
                    color="royalblue", marker="o", linewidth=2, ax=ax)
        ax.set_title("Waktu Puncak Peminjaman Sepeda dalam Sehari", fontsize=14, fontweight="bold")
        ax.set_xlabel("Jam")
        ax.set_ylabel("Total Peminjaman Sepeda")
        ax.set_xticks(range(0, 24))
        ax.grid(ls="--", alpha=0.7)
        
        st.pyplot(fig)  # Menampilkan grafik dengan benar
    else:
        st.warning("⚠️ Data jam peminjaman tidak tersedia dalam dataset ini.")
        
    st.markdown("""
    **📌 Kesimpulan**:
    - Jam sibuk peminjaman sepeda terjadi pada pukul 07:00 - 08:00 dan 17:00 - 18:00, yang bertepatan dengan waktu berangkat dan pulang.
    - Setelah pukul 20:00, jumlah peminjaman sepeda menurun drastis, menunjukkan bahwa sepeda lebih sering digunakan di pagi dan sore hari.
    """)


# 🎨 Sidebar Profil dengan Tampilan Menarik
st.sidebar.markdown(
    """
    <style>
        .sidebar-img img {
            border-radius: 100%;
            display: block;
            margin: auto;
            width: 150px; /* Sesuaikan ukuran */
            height: 150px; /* Sesuaikan ukuran */
            object-fit: cover; /* Memastikan gambar tetap proporsional */
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '<div class="sidebar-img"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFnvacQ6J2Mv5tqI4xWXPHQtzs33C7fkNMCw&s"></div>',
    unsafe_allow_html=True
)

st.sidebar.markdown("""
---                    
## 👤 **My Profile**
👋 **Nama** : Aryo Daffa Khairuddin  
📧 **Email**: [aryodaffakha48@gmail.com](mailto:aryodaffakha48@gmail.com)  
🏅 **ID Dicoding**: aryo09  

---

## 📌 **Tentang Saya**:  
Saya adalah seorang Machine Learning Engineer. Saya suka menganalisis data dan membuat visualisasi yang menarik!  
""")

st.sidebar.markdown("---")
st.sidebar.markdown(" **Terimakasih sudah mengunjungi dashboard ini!**")
