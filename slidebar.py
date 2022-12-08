import streamlit as st

# Crear el título para aplicación web
st.title('Mi Primera App con Streamlit')
sidebar = st.sidebar
sidebar.title('Esta es la barra lateral.')
sidebar.write('Aquí van los elementos de entrada')

st.header('Información sobre el Conjunto de Datos')

st.header('Descripción de los datos')

st.write("""
Este es un simple ejemplo de una app para predecir
¡Esta app predice mis datos!
""")

#La primera instrucción que tendrá nuestro archivo es la importación de la librería streamlit.
import streamlit as st

#La segunda intrucción es crear un título para nuestra aplicación.
st.title('Mi Primera App con Streamlit')

#Posteriormente vamos a crear una sección del lado derecho que se denomina barra lateral o sidebar en inglés. Para esto se utiliza la siguiente instrucción:
sidebar = st.sidebar

#Ya que tenemos creada la barra lateral, lo que tenemos que agregar es un título y un
#párrafo que explique que es lo que vamos a encontrar en dicha sección. Y las
#instrucciones para hacer eso se muestran a continuación:
sidebar.title("Esta es la barra lateral.")
sidebar.write("Aquí van los elementos de entrada.")

#Ahora bien, vamos a generar unos subtitulos que nos ayuden a dar más contexto sobre
#nuestra aplicación y para hacerlo vamos a utilizar la instrucción st.header. A continuación,
#se muestran las dos instrucciones que se utilizaron:
st.header("Información sobre el Conjunto de Datos")
st.header("Descripción de los datos ")

#Finalmente vamos a poner un pequeño párrafo que nos ayude a mostrar una breve
#descripción de nuestra aplicación web. Para lo cual vamos a utilizar la instrucción que ya
#habíamos visto en el tema anterior, st.write. A continuación se muestra dicha instrucción:
st.write("""
Este es un simple ejemplo de una app para predecir
¡Esta app predice mis datos!
""")
