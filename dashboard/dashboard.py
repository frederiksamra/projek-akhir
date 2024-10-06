import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Mengambil data
@st.cache_data
def load_data():
    day_df = pd.read_csv("https://raw.githubusercontent.com/frederiksamra/analisis-data-dengan-python/fa5df26b3147871f2918b3c02c7b3024b30aaf0f/day.csv")
    hour_df = pd.read_csv("https://raw.githubusercontent.com/frederiksamra/analisis-data-dengan-python/refs/heads/main/hour.csv")
    return day_df, hour_df

# Memuat data
day_df, hour_df = load_data()

# Judul Dashboard
st.title("Dashboard Penyewaan Sepeda")

# Menampilkan data summary
if st.checkbox("Tampilkan Data Hari"):
    st.subheader("Data Penyewaan Sepeda Per Hari")
    st.write(day_df)

if st.checkbox("Tampilkan Data Jam"):
    st.subheader("Data Penyewaan Sepeda Per Jam")
    st.write(hour_df)

# 1. Analisis Berdasarkan Kondisi Cuaca
st.subheader("Total Penyewaan Sepeda Berdasarkan Kondisi Cuaca")

# Agregasi data
dayweather_agg = day_df.groupby('weathersit').agg({'cnt': 'sum'}).reset_index()

# Menampilkan pie chart
st.subheader("Persentase Penyewaan Sepeda Berdasarkan Kondisi Cuaca")

# Membuat pie chart
fig, ax = plt.subplots(figsize=(8, 8))
y = dayweather_agg['cnt']  # Data untuk pie chart
x = dayweather_agg['weathersit']  # Label untuk pie chart (kondisi cuaca)

# Membuat pie chart dengan format persentase
ax.pie(y, labels=x, autopct='%1.1f%%', startangle=90, colors=['#6499E9', '#FFA07A', '#90EE90', '#FFD700'])

# Menambahkan judul
ax.set_title('Persentase Penyewaan Sepeda Berdasarkan Kondisi Cuaca')

# Menampilkan pie chart dalam Streamlit
st.pyplot(fig)

# 2. Total Penyewaan Sepeda Berdasarkan Jam
st.subheader("Total Penyewaan Sepeda Berdasarkan Jam")

# Agregasi data berdasarkan jam
hourweather_agg = hour_df.groupby('hr').agg({'cnt': 'sum'}).reset_index()

# Plot data
fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.bar(hourweather_agg['hr'], hourweather_agg['cnt'], color='#6499E9')
ax2.set_xticks(np.arange(min(hourweather_agg['hr']), max(hourweather_agg['hr'])+1, 1))
ax2.set_title('Total Penyewaan Sepeda Berdasarkan Jam')
ax2.set_xlabel('Jam')
ax2.set_ylabel('Total Penyewaan Sepeda')

# Menampilkan chart di Streamlit
st.pyplot(fig2)

# 3. Total Penyewaan Sepeda Berdasarkan Hari
st.subheader("Total Penyewaan Sepeda Berdasarkan Hari")

# Agregasi data berdasarkan hari
day_agg = day_df.groupby('weekday').agg({'cnt': 'sum'}).reset_index()

# Plot data
fig3, ax3 = plt.subplots(figsize=(8, 6))
ax3.bar(day_agg['weekday'], day_agg['cnt'], color='#6499E9')
ax3.set_xticks(np.arange(min(day_agg['weekday']), max(day_agg['weekday'])+1, 1))
ax3.set_title('Total Penyewaan Sepeda Berdasarkan Hari')
ax3.set_xlabel('Hari')
ax3.set_ylabel('Total Penyewaan Sepeda')

# Menampilkan chart di Streamlit
st.pyplot(fig3)

# 4. Insight dan Kesimpulan
st.subheader("Insight dan Kesimpulan")
st.write("""
Berdasarkan analisis, dapat dilihat bahwa kondisi cuaca sangat mempengaruhi total penyewaan sepeda. 
Semakin baik kondisi cuaca, semakin tinggi jumlah penyewaan sepeda.
""")
