import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

from src.data_loader import load_data

df = load_data()

st.title("📊 Insights")

st.subheader("Statistical Summary")

st.dataframe(df.describe())

numeric_df = df.select_dtypes(
    include=["int64","float64"]
)

if len(numeric_df.columns) > 1:

    st.subheader("Correlation Heatmap")

    fig, ax = plt.subplots(
        figsize=(10,6)
    )

    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

    st.pyplot(fig)
