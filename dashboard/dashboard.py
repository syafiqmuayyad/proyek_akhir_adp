import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(proyek_akhir_adp/dashboard/main_data.csv)

st.title("Bike Sharing Dashboard")

st.sidebar.header("Filter options")

selected_year = st.sidebar.selectbox("Select Year", data['year'].unique())
selected_month = st.sidebar.selectbox("Select Month", data['month'].unique())

selected_season = st.sidebar.multiselect("Select Season", data['season'].unique(), default=data['season'].unique())

selected_weather = st.sidebar.multiselect("Select Weather Condition", data['weathersit'].unique(), default=data['weathersit'].unique())

filtered_data = data[(data['year'] == selected_year) & 
                     (data['month'] == selected_month) & 
                     (data['season'].isin(selected_season)) & 
                     (data['weathersit'].isin(selected_weather))]

st.subheader(f"Showing data for {selected_month} {selected_year}")

st.dataframe(filtered_data)

st.subheader("Temperature Overview")

fig, ax = plt.subplots()
ax.plot(filtered_data['date'], filtered_data['temperature'], label='Temperature', color='orange')
ax.set_xlabel('Date')
ax.set_ylabel('Temperature')
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("Working vs Non-Working Days")
workingday_count = filtered_data['workingday'].value_counts()

st.bar_chart(workingday_count)

st.subheader("Weather Condition Breakdown")
weather_count = filtered_data['weathersit'].value_counts()

st.bar_chart(weather_count)

st.sidebar.markdown("Data source: Uploaded CSV")
