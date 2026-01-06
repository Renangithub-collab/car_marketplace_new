import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

import streamlit as st
from rsc.funcoes import carregar_dados, grafico_histograma

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
    fig = grafico_histograma(car_data, "odometer")
    st.plotly_chart(fig, use_container_width=True)
