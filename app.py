import streamlit as st
pip install streamlit git+https://github.com/streamlit/gsheets-connection
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load (link):
    #data = pd.read_csv('train.csv', nrows=nrows)
    url = link
    conn = st.experimental_connection("gsheets", type=GSheetsConnection)
    data = conn.read(spreadsheet=url)
    return data

ld = load("https://docs.google.com/spreadsheets/d/1Q3JpZ76p3_B2kWdP23373GzhpJ9kQhqGNvuad-6fHUc/edit?usp=sharing")


st.title("E-Commerce Data Visualization")
#st.bar_chart(ld["Product"])
st.dataframe(ld)

fig = plt.figure(figsize=(10, 10))
sns.countplot(x= "Product", data=ld)
st.pyplot(fig)



#st.title("E-Commerce Data Visualization")
#st.dataframe(data)
