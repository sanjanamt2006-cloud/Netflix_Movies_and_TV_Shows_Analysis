import streamlit as st
from src.data_loader import load_data
from src.charts import histogram
from src.charts import boxplot
from src.charts import scatter

df = load_data()

st.title("📈 Data Visualizations")

numeric_cols = df.select_dtypes(
    include=["int64","float64"]
).columns.tolist()

if len(numeric_cols) > 0:

    st.subheader("Histogram")

    col = st.selectbox(
        "Select Column",
        numeric_cols
    )

    st.plotly_chart(
        histogram(df,col),
        use_container_width=True
    )

    st.subheader("Box Plot")

    st.plotly_chart(
        boxplot(df,col),
        use_container_width=True
    )

    if len(numeric_cols) >= 2:

        x = st.selectbox(
            "X Axis",
            numeric_cols,
            key="x"
        )

        y = st.selectbox(
            "Y Axis",
            numeric_cols,
            key="y"
        )

        st.plotly_chart(
            scatter(df,x,y),
            use_container_width=True
        )
