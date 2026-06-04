import streamlit as st
from src.data_loader import load_data
from src.analysis import dataset_summary

st.title("📌 Dataset Overview")

df = load_data()

summary = dataset_summary(df)

col1,col2,col3,col4 = st.columns(4)

col1.metric("Rows", summary["Rows"])
col2.metric("Columns", summary["Columns"])
col3.metric("Missing", summary["Missing Values"])
col4.metric("Duplicates", summary["Duplicate Rows"])

st.subheader("Dataset Preview")

st.dataframe(df.head())

st.subheader("Data Types")

st.dataframe(df.dtypes.astype(str))
