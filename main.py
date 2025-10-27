import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(layout="wide")
st.title("Data Visualization with PyGWalker")

df = pd.read_csv('assignment.csv')

pyg_app = StreamlitRenderer(df)
pyg_app.explorer() 

hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

