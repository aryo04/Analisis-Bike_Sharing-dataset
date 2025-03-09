import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

# Load datasets
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Streamlit app
st.title("Dashboard Pinjaman Sepeda")
st.subheader("Proyek Analisis Data: [Bike Sharing Dataset]")
st.markdown("""
            - Pertanyaan 1 : Bagaimana pengaruh **cuaca** terhadap **jumlah peminjaman sepeda**?
            - Pertanyaan 2 : Bagaimana pola peminjaman sepeda berdasarkan **jam** (24 jam)?""")

tab1, tab2 = st.tabs(["Analisis Pertanyaan 1", "Analisis Pertanyaan 2"])

with tab1:

    # Menampilkan bar chart total pinjaman sepeda berdasarkan cuaca
    st.subheader("Total Pinjaman Sepeda Berdasarkan Cuaca")
    fig, ax = plt.subplots()
    weathercnt = day_df.groupby('weathersit')['cnt'].sum()
    sns.barplot(x=weathercnt.index, y=weathercnt.values, ax=ax)
    ax.set_xlabel("Kategori Cuaca")
    ax.set_ylabel("Total Pinjaman Sepeda")
    st.pyplot(fig)

    # Menampilkan boxplot chart distribusi pinjaman sepeda berdasarkan cuaca
    st.subheader("Distribusi Peminjaman Sepeda Berdasarkan Cuaca")
    fig, ax = plt.subplots()
    ax.set_xlabel("Kategori Cuaca")
    ax.set_ylabel("Jumlah Pinjaman Sepeda")
    sns.boxplot(data=day_df, x='weathersit', y='cnt', ax=ax)
    st.pyplot(fig)

    #simpulan
    st.subheader("Simpulan Analisis Pertanyaan 1")
    st.markdown("""
                Dapat kita lihat pada data korelasi, atribut cuaca (weathersit) 
                dan jumlah pinjaman (cnt) hasil nya yaitu -0.29 yang artinya jika 
                nilai korelasi negatif maka kedua atribut itu berlawanan dan 
                karena mendekati 0 maka kedua atribut tersebut tidak berkorelasi (lemah)
    """)

with tab2:
    # Menampilkan line chart rata-rata peminjaman sepeda berdasarkan jam
    st.subheader("Rata-rata Peminjaman Sepeda Berdasarkan Jam")
    fig, ax = plt.subplots()
    hourly_avg = hour_df.groupby('hr')['cnt'].mean()
    ax.plot(hourly_avg.index, hourly_avg.values, marker='o')
    plt.xticks(range(0, 24))
    ax.set_xlabel("Jam pinjaman")
    ax.set_ylabel("Rata-rata Peminjaman")
    st.pyplot(fig)

    #simpulan
    st.subheader("Simpulan Analisis Pertanyaan 2")
    st.markdown("""
                Jumlah peminjam paling banyak yaitu pada pagi hari, dan sore 
                menjelang malam. Sedangkan jumlah peminjam paling sedikit 
                yaitu ketika pada malam atau dini hari.
    """)

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://th.bing.com/th/id/OIP.KNBmOhko0EgUIhoAjllq6AHaFZ?w=280&h=204&c=7&r=0&o=5&dpr=1.5&pid=1.7")
    #  profil saya
    st.markdown("""
        # [Bike Sharing Dataset]
            - Nama: Fakhira Lahen Siregar
            - Email: fahiralahens@gmail.com
            - ID Dicoding: fakhiralahensiregar
    """)
    
    
