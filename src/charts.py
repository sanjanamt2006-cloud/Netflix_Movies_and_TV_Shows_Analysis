import plotly.express as px
import pandas as pd

def histogram(df, column):

    fig = px.histogram(
        df,
        x=column,
        template="plotly_dark"
    )

    return fig


def boxplot(df, column):

    fig = px.box(
        df,
        y=column,
        template="plotly_dark"
    )

    return fig


def scatter(df, x_col, y_col):

    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        color=y_col,
        template="plotly_dark"
    )

    return fig
