import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "main_data.csv"
df = pd.read_csv(file_path)

# Mapping Musim & Cuaca
season_mapping = {
    "Musim Semi": "Spring",
    "Musim Panas": "Summer",
    "Musim Gugur": "Fall",
    "Musim Dingin": "Winter"
}

weather_mapping = {
    "Cerah": "Clear",
    "Berawan": "Cloudy",
    "Hujan Ringan": "Light Rain",
    "1": "Clear",
    "2": "Cloudy",
    "3": "Light Rain",
}


df["season"] = df["season"].map(season_mapping)
df["weathersit"] = df["weathersit"].map(weather_mapping)

colors = {"Clear": "#E1812C", "Cloudy": "#3274A1", "Light Rain": "#3A923A"}

# Title
st.title("🚴‍♂ Bike Sharing Dashboard")

# Create tabs
tab1, tab2 = st.tabs(["📊 Tren Peminjaman", "⏳ Jam Puncak Peminjaman"])

with tab1:
    mode = st.radio("Pilih Mode Tampilan:", ["Per Musim", "Semua Musim"], horizontal=True)

    if mode == "Per Musim":
        season_options = df["season"].dropna().unique()
        selected_season = st.radio("Pilih Musim:", season_options, horizontal=True)
        filtered_df = df[df["season"] == selected_season]

        st.subheader(f"Jumlah Peminjaman Sepeda pada {selected_season}")
        plt.figure(figsize=(10,6)) 
        ax = sns.barplot(data=filtered_df, x="weathersit", y="cnt", ci=None, palette=colors)
        plt.xlabel("Kondisi Cuaca")
        plt.ylabel("Jumlah Peminjaman Sepeda")
        plt.title(f"Jumlah Peminjaman Sepeda Berdasarkan Cuaca di {selected_season}")
        
        # Menambahkan legend
        handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in colors]
        plt.legend(handles, colors.keys(), title="Cuaca", loc="upper right")
        
        st.pyplot(plt)


        # Kesimpulan per musim
        most_rented_weather = filtered_df.groupby("weathersit")["cnt"].sum().idxmax()
        least_rented_weather = filtered_df.groupby("weathersit")["cnt"].sum().idxmin()

        st.markdown(f"""
        📌 **Kesimpulan Musim {selected_season}**:
        - Pada **{selected_season}** dengan kondisi cuaca **{most_rented_weather}** memiliki jumlah peminjaman terbanyak. Sementara itu, dengan kondisi cuaca **{least_rented_weather}** memiliki jumlah peminjaman paling sedikit.
        """)
        
    else:
        st.subheader("Tren peminjaman sepeda berdasarkan musim dan kondisi cuaca")
        plt.figure(figsize=(10, 6))
        sns.barplot(data=df, x="season", y="cnt", hue="weathersit", ci=None, palette=colors)
        plt.xlabel("Musim")
        plt.ylabel("Jumlah Peminjaman Sepeda")
        plt.title("Perbandingan Peminjaman Sepeda di Setiap Musim Berdasarkan Cuaca")
        plt.legend(title="Cuaca", loc="upper left")
        st.pyplot(plt)

        # Kesimpulan semua musim
        most_rented_season = df.groupby("season")["cnt"].sum().idxmax()
        least_rented_season = df.groupby("season")["cnt"].sum().idxmin()

        # Menentukan cuaca dengan peminjaman tertinggi dan terendah
        most_rented_weather = df.groupby("weathersit")["cnt"].sum().idxmax()
        least_rented_weather = df.groupby("weathersit")["cnt"].sum().idxmin()

        st.markdown(f"""
        *📌 Kesimpulan Keseluruhan*:
        - Pada **{most_rented_season}** memiliki jumlah peminjaman tertinggi. Sedangkan, pada **{least_rented_season}** memiliki jumlah peminjaman terendah. Dengan kondisi cuaca **{most_rented_weather}** menjadi kondisi paling ideal untuk peminjaman sepeda, sementara saat **{least_rented_weather}** jumlah peminjaman paling terendah. 
        - Hal ini menunjukkan bahwa musim dan cuaca sangat berpengaruh terhadap jumlah peminjaman sepeda.
        """)

with tab2:
    st.subheader("Pada jam berapa peminjaman sepeda mencapai puncaknya dalam sehari?")
    
    if "hr" in df.columns and df["hr"].notna().sum() > 0:
        df_hourly = df.dropna(subset=["hr"])
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(x="hr", y="cnt", data=df_hourly, estimator="sum", ci=None, 
                     color="royalblue", marker="o", linewidth=2, ax=ax)
        ax.set_title("Waktu Puncak Peminjaman Sepeda dalam Sehari", fontsize=14, fontweight="bold")
        ax.set_xlabel("Jam")
        ax.set_ylabel("Total Peminjaman Sepeda")
        ax.set_xticks(range(0, 24))
        ax.grid(ls="--", alpha=0.7)
        st.pyplot(fig)
    else:
        st.warning("⚠ Data jam peminjaman tidak tersedia dalam dataset ini.")
    
    st.markdown("""
    *📌 Kesimpulan*:
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
            width: 150px;
            height: 150px;
            object-fit: cover;
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
## *My Profile*
👋 *Nama* : Aryo Daffa Khairuddin  
📧 *Email*: [aryodaffakha48@gmail.com](mailto:aryodaffakha48@gmail.com)  
🔖 *ID Dicoding*: aryo09  

---

## *About Me*
Saya adalah seorang Machine Learning Engineer. Saya suka menganalisis data dan membuat visualisasi yang menarik!  
""")

st.sidebar.markdown("---")
st.sidebar.markdown(" *Terimakasih sudah mengunjungi dashboard ini!*")
