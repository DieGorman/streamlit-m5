import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

titanic = ('titanic.csv')
titanic_data = pd.read_csv(titanic)

st.dataframe(titanic_data) 
st.header("Data Description")

fig, ax = plt.subplots() #Inicializa la variable fig que contendrá el histograma y la variable ax que nos servirá para construirlo.
ax.hist(titanic_data.Fare) #Nos permite construir el histograma con el campo “fare” de la base de datos del Titanic.
st.header("Histograma del Titanic") #st.header nos sirve para poner un encabezado para nuestra gráfica.
st.pyplot(fig) #La instrucción st.pyplot nos ayude a graficar nuestro histograma en streamlit.
st.markdown("___") # st.markdown nos ayuda a generar una línea que sirva de división para nuestra gráfica.

fig2, ax2 = plt.subplots() #Inicializa la variable fig que contendrá la gráfica de barras y la variable ax que nos servirá para construirlo.
y_pos = titanic_data['Pclass'] #Las variables x_pos y y_pos nos sirven para cargar los datos que corresponden a los campos
x_pos = titanic_data['Fare'] #“class” y “fare” respectivamente y que vamos a pasarle a la gráfica de barras.
ax2.barh(y_pos, x_pos) #ax2.barh nos sirve para generar una gráfica de barras horizontal que contendrá los campos antes mencionados. 
ax2.set_ylabel("Class") #ax2.set_xlabel y ax2.set_ylabel nos sirven para poner etiquetas para el eje de las x y el de las y
ax2.set_xlabel("Fare")
ax2.set_title('¿Cuanto pagaron las clases del Titanic') # ax2.set_title nos ayuda a poner un título para nuestra gráfica.
st.header("Grafica de Barras del Titanic") #st.header nos sirve para colocar un título para nuestra gráfica.
st.pyplot(fig2) #st.pyplot es la que le indica a Streamlit la gráfica que va a visualizar. 
st.markdown("___")

fig3, ax3 = plt.subplots() #inicializa la variable fig que contendrá la gráfica de dispersión y la variable ax que nos servirá para construirlo.
ax3.scatter(titanic_data.Age, titanic_data.Fare) #ax3.scatter es la instrucción de Matplotlib que nos sirve para construir una gráfica 
#de dispersión y esta recibe dos parámetros que en este caso serán los campos “age” y “fare”
ax3.set_xlabel("Edad") #ax3.set_xlabel y ax3.set_ylabel nos permiten colocar etiquetas en el eje de las x y en el eje de las y. 
ax3.set_ylabel("Tarifa")
st.header("Grafica de Dispersión del Titanic") 
st.pyplot(fig3)