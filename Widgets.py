import pandas as pd
import streamlit as st

st.title('Radio Button o Botón de Opción')
DATA_URL = ('titanic.csv')

data = pd.read_csv(DATA_URL)

st.header("Dataset Overview Titanic")
st.dataframe(data)

#Botones de opciones o radiobuttons
selected_class = st.radio("Select Class", data['Pclass'].unique())
st.write("Selected Class:", selected_class)

#Casilla de Verificación o Selectbox
selected_sex = st.selectbox("Select Sex", data['Sex'].unique())
st.write(f"Selected Option: {selected_sex!r}")

#Control deslizante o slider
optionals = st.expander("Optional Configurations", True)
fare_select = optionals.slider(
    "Select the Fare",
    min_value=float(data['Fare'].min()),
    max_value=float(data['Fare'].max())
)
subset_fare = data[(data['Fare'] >= fare_select)]
st.write(f"Number of Records With this Fare {fare_select}: {subset_fare.shape[0]}")