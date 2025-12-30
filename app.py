import os
import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# Importa funções diretamente do módulo local
try:
    from rsc.funcoes import carregar_dados, criar_histograma
except ImportError:
    # Fallback para desenvolvimento local
    import sys
    sys.path.append(".")
    from rsc.funcoes import carregar_dados, criar_histograma

st.set_page_config(page_title="Car Marketplace", layout="centered")
st.title("🚗 Análise de Anúncios de Carros")

# Caminho FIXO para o Render - NÃO use '..'
# 1. Tenta caminho relativo (para Render)
# 2. Tenta caminho absoluto (fallback)
DATA_PATH = "data/vehicles_us.csv"
if not os.path.exists(DATA_PATH):
    # Fallback para desenvolvimento local
    DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "vehicles_us.csv")

# Verifica se arquivo existe
if not os.path.exists(DATA_PATH):
    st.error(f"Arquivo CSV não encontrado em: {DATA_PATH}")
    st.stop()

car_data = carregar_dados(DATA_PATH)

st.write("### Visualização inicial dos dados")
st.dataframe(car_data.head())

if st.checkbox("Mostrar histograma do odômetro"):
    fig = criar_histograma(car_data, "odometer")
    st.pyplot(fig)