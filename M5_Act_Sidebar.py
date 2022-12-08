import streamlit as st
import pandas as pd

DATA_URL = ('walmart.csv')
data = pd.read_csv(DATA_URL)

st.title('Análisis de datos de Walmart USA')
st.header('Información sobre el Conjunto de Datos')
st.write('Predicción de ventas de productos de línea blanca en el noroeste de los Estados Unidos.')

sidebar = st.sidebar
sidebar.title('Checkboxes')
sidebar.header('Palomea la opción deseada')

sidebar.title('Selectboxes')
sidebar.header('Selecciona la opción deseada')

#Botones de opciones o radiobuttons
selected_ship_mode = st.radio("Select Ship Mode", data['Ship Mode'].unique())
st.write("Selected Class:", selected_ship_mode)

#Casilla de Verificación o Selectbox
selected_category = st.selectbox("Select Category", data['Category'].unique())
st.write(f"Selected Option: {selected_category!r}")

#Control deslizante o slider
optionals = st.expander("Optional Configurations", True)
discount_select = optionals.slider(
    "Select Discount",
    min_value=float(data['Discount'].min()),
    max_value=float(data['Discount'].max())
)
subset_discount = data[(data['Discount'] >= discount_select)]
st.write(f"Number of Records With this Discount {discount_select}: {subset_discount.shape[0]}")