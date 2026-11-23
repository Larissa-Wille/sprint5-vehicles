
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Análise de anúncios de veículos",
    layout="wide"
)

st.title("Análise de anúncios de veículos")
st.write(
    "Explore a distribuição dos preços e a relação "
    "entre quilometragem e preço dos veículos anunciados."
)

@st.cache_data
def carregar_dados():
    return pd.read_csv("vehicles_us.csv")

car_data = carregar_dados()

st.write(f"Total de anúncios: {len(car_data):,}")

if st.checkbox("Mostrar histograma de preços"):
    fig = px.histogram(
        car_data,
        x="price",
        nbins=50,
        title="Distribuição dos preços dos veículos",
        labels={"price": "Preço (US$)"}
    )
    st.plotly_chart(fig, width="stretch")

if st.checkbox("Mostrar gráfico de dispersão"):
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        opacity=0.5,
        title="Relação entre quilometragem e preço",
        labels={
            "odometer": "Quilometragem",
            "price": "Preço (US$)"
        }
    )
    st.plotly_chart(fig, width="stretch")