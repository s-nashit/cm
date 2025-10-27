import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(layout="wide")
st.title("Data Visualization with PyGWalker")

df = pd.read_csv('assignment.csv')

pyg_app = StreamlitRenderer(df)
pyg_app.explorer() 

