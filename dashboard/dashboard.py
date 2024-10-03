import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

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

# Mempersiapkan data
dayweather_agg = day_df.groupby('weathersit').agg({'cnt': 'sum'}).reset_index()
hourweather_agg = hour_df.groupby('hr').agg({'cnt': 'sum'}).reset_index()

# Menampilkan data summary
if st.checkbox("Tampilkan Data Hari"):
    st.subheader("Data Penyewaan Sepeda Per Hari")
    st.write(day_df)

if st.checkbox("Tampilkan Data Jam"):
    st.subheader("Data Penyewaan Sepeda Per Jam")
    st.write(hour_df)

# Analisis berdasarkan kondisi cuaca
st.subheader("Total Penyewaan Sepeda Berdasarkan Kondisi Cuaca")

# Agregasi data
dayweather_agg = day_df.groupby('weathersit').agg({'cnt': 'sum'})

# Plot data
fig, ax = plt.subplots()
y = dayweather_agg[('cnt')]
x = dayweather_agg.index

ax.bar(x, y, color='#6499E9')
ax.set_xticks(np.arange(min(x), max(x)+1, 1))
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
plt.title('Total Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Total Penyewaan Sepeda')

# Total Penyewaan Sepeda Berdasarkan Jam
st.subheader("Total Penyewaan Sepeda Berdasarkan Jam")
fig2, ax2 = plt.subplots()
ax2.bar(hourweather_agg['hr'], hourweather_agg['cnt'], color='#6499E9')
ax2.set_xlabel('Jam')
ax2.set_ylabel('Total Penyewaan Sepeda')
ax2.set_title('Total Penyewaan Sepeda Berdasarkan Jam')
st.pyplot(fig2)

# Total Penyewaan Sepeda Berdasarkan Hari
st.subheader("Total Penyewaan Sepeda Berdasarkan Hari")
day_agg = day_df.groupby('weekday').agg({'cnt': 'sum'}).reset_index()
fig3, ax3 = plt.subplots()
ax3.bar(day_agg['weekday'], day_agg['cnt'], color='#6499E9')
ax3.set_xlabel('Hari')
ax3.set_ylabel('Total Penyewaan Sepeda')
ax3.set_title('Total Penyewaan Sepeda Berdasarkan Hari')
st.pyplot(fig3)

# Menampilkan plot
st.pyplot(fig)

# Menampilkan informasi lebih lanjut
st.subheader("Insight dan Kesimpulan")
st.write("""
Berdasarkan analisis, dapat dilihat bahwa kondisi cuaca sangat mempengaruhi total penyewaan sepeda. 
Semakin baik kondisi cuaca, semakin tinggi jumlah penyewaan sepeda.
""")
