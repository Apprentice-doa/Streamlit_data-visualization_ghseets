import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

@st.cache_data
def load (link):
    url = link
    conn = st.experimental_connection("gsheets", type=GSheetsConnection)
    data = conn.read(spreadsheet=url)
    return data

ld = load("https://docs.google.com/spreadsheets/d/1Q3JpZ76p3_B2kWdP23373GzhpJ9kQhqGNvuad-6fHUc/edit?usp=sharing")





image = Image.open('cart.png')

st.image(image, width=100)
st.header("E-Commerce Data Analysis and  Visualization")
st.dataframe(ld)

fig = plt.figure(figsize=(10, 10))
sns.countplot(x= "Product", data=ld)
st.pyplot(fig)

