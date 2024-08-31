import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Proyecto Web Page')
st.write('Esta aplicación aún no es funcional. En construcción.')



hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir diagrama de dispercion')
if scatter_button:
    st.write('Creación de un diagrama de dispercion para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price") 
    st.plotly_chart(fig, use_container_width=True)