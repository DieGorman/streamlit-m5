import pandas as pd
import streamlit as st
import numpy as np

DATE_COLUMN = 'Date/Time'
uber = ('uber_dataset.csv')

st.title('Uber pickups in NYC')
st.header('Usando Streamlit y Mapbox')
st.write('Viajes de Uber en la ciudad de Nueva York con filtros por hora')

@st.cache
def load_data(nrows):
    data = pd.read_csv(uber, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text("Done! (using st.cache)")

#Control deslizante o slider
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
