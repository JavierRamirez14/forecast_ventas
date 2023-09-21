from codigo_produccion import *
import streamlit as st
import pandas as pd
from datetime import timedelta
import io

#CONFIGURACION DE LA PÁGINA
st.set_page_config(
     page_title = 'Javier Ramírez - Forecast de Ventas',
     page_icon = 'logo.png',
     layout = 'wide')

@st.cache
def crear_df(df, fecha_inicio, fecha_fin):
    fecha_inicio_df = fecha_inicio - timedelta(days=30)
    df = df.loc[(df.date >= fecha_inicio_df) & (df.date <= fecha_fin)]
    return df

@st.cache
def calcular_ventas(df):
    df_predicciones = ejecutar_todo(df)
    return df_predicciones  # Debes retornar los resultados de las predicciones

st.title('FORECAST DE VENTAS')
st.write('Esta aplicación se utiliza para realizar predicciones de ventas en el contexto de una cadena de alimentos minorista en Ecuador. Te invito a explorar su funcionamiento. El único requisito es que las predicciones solo pueden ser desde el 31 de Julio de 2017 al 15 de Agosto de 2017.')
with st.sidebar:
    st.sidebar.image('logo.png', width=150)
    fecha_inicio = st.date_input('Fecha de inicio de las predicciones:')
    fecha_inicio = pd.to_datetime(fecha_inicio)
    fecha_fin = st.date_input('Fecha final de las predicciones:')
    fecha_fin = pd.to_datetime(fecha_fin)

if st.sidebar.button('CALCULAR VENTAS'):
    with open('df_app.pickle', mode='rb') as file:
       df_app = pickle.load(file)
    df_usuario = crear_df(df_app, fecha_inicio, fecha_fin)
    df_predicciones = calcular_ventas(df_usuario)
    st.write(df_predicciones)
else:
    st.stop()
