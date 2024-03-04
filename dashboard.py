import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_lottie import st_lottie

#set page
st.set_page_config(page_title="Rental Sepeda", page_icon=":mouth:", layout="wide")

#load assets
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_sepeda = load_lottieurl("https://lottie.host/bd2bde5d-8ef6-4e15-908e-d05baf203ecb/ctWuGE3vTo.json")
lottie_logo = load_lottieurl("https://lottie.host/58b0aefc-f745-4b73-9db1-01b80d621acd/k6JtZyPQEJ.json")

#load berkas
data_day = pd.read_csv("day.csv")


#Header section
st.title("Dashboard Rental Sepeda :bike:")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Apa itu dashboard rental sepeda?")
        st.write("Dashboard rental sepeda merupakan dashboard yang dapat menampilkan data rental sepeda dalam kurun waktu dua tahun terakhir. Kamu bisa gunakan ini untuk menentukan kapan banyak orang bersepeda.")
        st.subheader("Bagaimana caranya?")
        st.write("Cukup pilih rentang tanggal yang datanya mau kamu lihat, kamu sudah bisa melihat dashboard rental sepeda.")
    with right_column:
        st_lottie(lottie_sepeda, height=300, key="sepeda")
        
#sesi pilih data    
data_day['dteday'] = pd.to_datetime(data_day['dteday'])    

date_min = data_day["dteday"].min()
date_max = data_day["dteday"].max()

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(lottie_logo, height=300, key="logo")
    with right_column:
        st.subheader("Rentang Tanggal")
        st.write("Kamu bisa pilih dashboard sesuai tanggal yang kamu mau. Cukup pilih rentang tanggal di bawah ini ya!")
        start_date, end_date = st.date_input(
            label='Pilih Rentang Tanggal', min_value=date_min,
            max_value=date_max, value=[date_min, date_max]) 

#filtered
main_df = data_day[(data_day["dteday"] >= str(start_date)) & 
                (data_day["dteday"] <= str(end_date))]

with st.container():
    st.write("---")
    st.markdown("<h1 style='text-align: center;'>Dashboard Rental Sepeda</h1>", unsafe_allow_html=True)
    left_column, right_column = st.columns(2)
    with left_column:
    #buat grafik casual
        fig, ax = plt.subplots(figsize=(6,4))
        ax.plot(main_df['dteday'], main_df['casual'], marker='o', color='red')
        ax.set_xlabel("Tanggal")
        ax.set_ylabel("Jumlah Perental Sepeda")
        ax.set_title("Grafik Data Rental Sepeda Casual Per Hari")
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
    with right_column:
    #buat grafik registered
        fig, ax = plt.subplots(figsize=(6,4))
        ax.plot(main_df['dteday'], main_df['registered'], marker='o', color='blue')
        ax.set_xlabel("Tanggal")
        ax.set_ylabel("Jumlah Perental Sepeda")
        ax.set_title("Grafik Data Rental Sepeda Registered Per Hari")
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)

#buat grafik total keduanya
fig, ax = plt.subplots(figsize=(6,4))
ax.plot(main_df['dteday'], main_df['cnt'], marker='o', color='purple')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Perental Sepeda")
ax.set_title("Grafik Data Rental Sepeda Total Casual dan Registered Per Hari")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

st.write("---")
st.caption("Tugas Dicoding by Nur Afni Latifatul Muchlisa")