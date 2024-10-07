import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('dashboard/main_data.csv')

st.title("Bike Sharing Dashboard")

st.sidebar.header("Filter options")
selected_year = st.sidebar.selectbox("Select Year", data['year'].unique())
selected_month = st.sidebar.multiselect("Select Month", data['month'].unique(), default=data['month'].unique())
selected_season = st.sidebar.multiselect("Select Season", data['season'].unique(), default=data['season'].unique())
selected_weather = st.sidebar.multiselect("Select Weather Condition", data['weathersit'].unique(), default=data['weathersit'].unique())
selected_temperature_range = st.sidebar.multiselect("Select Temperature Range", data['temperature_range'].unique(), default=data['temperature_range'].unique())

filtered_data = data[(data['year'] == selected_year) & 
                     (data['month'].isin(selected_month)) & 
                     (data['season'].isin(selected_season)) & 
                     (data['weathersit'].isin(selected_weather)) & 
                     (data['temperature_range'].isin(selected_temperature_range))]

st.subheader(f"Showing data for year {selected_year}")
st.dataframe(filtered_data)

data['month'] = pd.to_datetime(data['date']).dt.month
filtered_data['month'] = pd.to_datetime(filtered_data['date']).dt.month

data['temperature_range'] = pd.cut(data['temperature'], bins=[0, 0.2, 0.4, 0.6, 0.8, 1], 
                                   labels=['Very Cold', 'Cold', 'Mild', 'Warm', 'Hot'])

avg_rentals_by_month = filtered_data.groupby('month')['cnt'].mean().reset_index()



st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Bulan")
fig, ax = plt.subplots()
sns.lineplot(x='month', y='cnt', data=avg_rentals_by_month, marker='o', color='b', ax=ax)
ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Bulan')
ax.set_xlabel('Bulan')
ax.set_ylabel('Rata-rata Penyewaan')
ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'])
ax.grid(True)
st.pyplot(fig)

avg_rentals_by_temperature = filtered_data.groupby('temperature_range', observed=True)['cnt'].mean().reset_index()

st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Suhu")
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x='temperature_range', y='cnt', data=avg_rentals_by_temperature, palette='coolwarm')
ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Suhu')
ax.set_xlabel('Kategori Suhu')
ax.set_ylabel('Rata-rata Penyewaan')
st.pyplot(fig)

avg_rentals_by_season = filtered_data.groupby('season')['cnt'].mean().reset_index()

st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x='season', y='cnt', data=avg_rentals_by_season, palette='coolwarm', ax=ax)
ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Musim')
ax.set_xlabel('Musim')
ax.set_ylabel('Rata-rata Penyewaan')
st.pyplot(fig)

avg_rentals_by_weather = filtered_data.groupby('weathersit')['cnt'].mean().reset_index()

st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x='weathersit', y='cnt', data=avg_rentals_by_weather, palette='coolwarm', ax=ax)
ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Rata-rata Penyewaan')
st.pyplot(fig)
