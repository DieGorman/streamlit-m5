import pandas as pd
import streamlit as st
import numpy as np

map_data = pd.DataFrame(np.random.randn(1000,2) / [50,50] + [37.76, -122.4], columns = ['lat','lon'])

st.title('Mapa de San Francisco')
st.header('Usando Streamlit y Mapbox')
st.map(map_data)