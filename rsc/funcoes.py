import pandas as pd
import plotly.express as px

def carregar_dados(caminho_csv):
    """Carrega o dataset de veículos"""
    return pd.read_csv(caminho_csv)

def grafico_histograma(df, coluna):
    """Histograma interativo"""
    fig = px.histogram(df, x=coluna, title=f'Histograma de {coluna}')
    return fig

def grafico_dispersao(df, x, y):
    """Gráfico de dispersão"""
    fig = px.scatter(df, x=x, y=y, title=f'{y} vs {x}')
    return fig
