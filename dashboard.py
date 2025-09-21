import streamlit as st
import pandas as pd

st.title("📢 Automated News Headlines Dashboard")

df = pd.read_csv("headlines.csv")

st.subheader("Latest 10 Headlines")
st.table(df.tail(10))

st.subheader("Dataset Overview")
st.write(df)
