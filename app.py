# force redeploy

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

import streamlit as st
from rsc.funcoes import carregar_dados, grafico_histograma, grafico_dispersao


st.set_page_config(page_title="Car Marketplace", layout="centered")
st.title("🚗 Análise de Anúncios de Carros")

DATA_PATH = "data/vehicles_us.csv"
if not os.path.exists(DATA_PATH):
    DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "vehicles_us.csv")

if not os.path.exists(DATA_PATH):
    st.error(f"Arquivo CSV não encontrado em: {DATA_PATH}")
    st.stop()

car_data = carregar_dados(DATA_PATH)

st.write("### Visualização inicial dos dados")
st.dataframe(car_data.head())

if st.checkbox("Mostrar histograma do odômetro"):

    limite = st.slider(
        "Limite máximo do odômetro",
        min_value=50000,
        max_value=500000,
        value=300000,
        step=10000
    )

    # Filtra para remover outliers e melhorar a visualização
    df_filtrado = car_data[car_data["odometer"] <= limite]

    fig = grafico_histograma(df_filtrado, "odometer")
    fig.update_layout(
        xaxis_title="Odômetro (milhas)",
        yaxis_title="Quantidade de veículos"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.caption(
        "A maioria dos veículos possui odometragem abaixo desse valor. "
        "Valores muito altos foram filtrados para facilitar a interpretação do histograma."
    )
st.header("📈 Gráfico de dispersão")

if st.checkbox("Mostrar gráfico de dispersão (Preço x Odômetro)"):

    df_disp = car_data.dropna(subset=["price", "odometer"])

    fig = grafico_dispersao(
        df_disp,
        x="odometer",
        y="price"
    )

    fig.update_layout(
        xaxis_title="Odômetro (milhas)",
        yaxis_title="Preço (USD)"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.caption(
        "Este gráfico mostra a relação entre a quilometragem dos veículos e seus preços."
    )
