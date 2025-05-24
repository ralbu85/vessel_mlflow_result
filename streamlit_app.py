import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. List all CSV files in the `data/` folder
data_dir = "data"
csv_files = [f for f in os.listdir(data_dir) if f.endswith(".csv")]
selected_file = st.selectbox("Select CSV file", csv_files)

# 2. Load selected CSV file
df = pd.read_csv(os.path.join(data_dir, selected_file))
st.success(f"Loaded {selected_file} with {len(df)} rows")


desired_order = ["none", "1h", "3h", "6h", "12h", "24h"]  # example
factors = ['downsample', 'split', 'target_feature', 'OutlierRemoval', 'environmental_features']
metrics = ["mae", "mape", "r2", "mse"]

# Selectors
color_feature = st.selectbox("Color By:", factors)
metric = st.selectbox("Metric:", metrics)  # adjust as needed

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