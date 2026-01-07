import pandas as pd
import plotly.express as px
import streamlit as st

@st.cache_data
def carregar_dados(caminho_csv):
    return pd.read_csv(caminho_csv)

def grafico_histograma(df, coluna):
    fig = px.histogram(df, x=coluna, title=f'Histograma de {coluna}')
    return fig

def grafico_dispersao(df, x, y):
    fig = px.scatter(
        df,
        x=x,
        y=y,
        title=f'{y} vs {x}'
    )
    return fig
