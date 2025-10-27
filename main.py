import streamlit as st
import pandas as pd
import pygwalker as pg
st.title('My Application')
df = pd.read_csv('assignment.csv')

st.write(df)
