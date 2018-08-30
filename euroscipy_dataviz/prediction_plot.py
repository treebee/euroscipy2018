import os
import logging

import altair as alt
import numpy as np
import pandas as pd


def load_predictions():
    path = os.path.join(
        os.path.dirname(__file__), os.pardir, "data/predictions_sales.csv"
    )
    df = pd.read_csv(path)
    df["date"] = df["date"].astype(np.datetime64)
    df["store_id"] = df["store_id"].astype(str)
    return df


def generate_plot(df):
    long_form = df.melt(
        id_vars=["date"],
        value_vars=["sales", "predictions"],
        var_name="Legend",
        value_name="pcs",
    )

    chart = (
        alt.Chart(long_form)
        .mark_line(point=True)
        .encode(x="date", y="pcs", color="Legend:N")
    )
    return chart
