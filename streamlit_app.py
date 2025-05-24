import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv("Vessel_full_factorial_nowcast_Linear_stdscaler.csv")  # or however you load it
desired_order = ["none", "1h", "3h", "6h", "12h", "24h"]  # example

# Selectors
color_feature = st.selectbox("Color By:", df.columns)
metric = st.selectbox("Metric:", ["RMSE", "MAE", "R2"])  # adjust as needed

# Hover info
hover_factors = [
    "OutlierRemoval",
    "target_feature",
    "environmental_features",
    "split",
    "downsample",
    "ship_name",
    metric
]

# Create the plot
fig = px.strip(
    df,
    x="ship_name",
    y=metric,
    color=color_feature,
    category_orders={"downsample": desired_order},
    title=f"{metric.upper()} by Ship and {color_feature}",
    stripmode="group",
    hover_data=hover_factors,
    height=600
)

fig.update_layout(
    xaxis_title="Ship Name",
    yaxis_title=metric.upper(),
    xaxis_tickangle=30,
    legend_title=color_feature
)

st.plotly_chart(fig, use_container_width=True)