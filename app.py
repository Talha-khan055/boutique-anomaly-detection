
import pickle
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Boutique Anomaly Detection",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ Boutique Transaction Anomaly Dashboard")
st.write("Explore transactions and identify unusual activity.")

DATA_PATH = Path("data/transactions.csv")
MODEL_PATH = Path("model.pkl")

# Load data and trained model
df = pd.read_csv(DATA_PATH)
df["date"] = pd.to_datetime(df["date"])

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

# Predict anomalies
df["predicted_anomaly"] = model.predict(df[["amount"]]) == -1

# Date range slider
min_date = df["date"].min().date()
max_date = df["date"].max().date()

selected_dates = st.slider(
    "Select transaction date range",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),
    format="YYYY-MM-DD"
)

# Filter transactions
filtered_df = df[
    (df["date"].dt.date >= selected_dates[0]) &
    (df["date"].dt.date <= selected_dates[1])
]

anomalies = filtered_df[filtered_df["predicted_anomaly"]]

# Summary metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Transactions", len(filtered_df))
col2.metric("Total Sales", f"{filtered_df['amount'].sum():,}")
col3.metric("Flagged Anomalies", len(anomalies))

# Anomaly table
st.subheader("Flagged Transactions")

if anomalies.empty:
    st.info("No anomalies found in this date range.")
else:
    st.dataframe(
        anomalies[
            ["date", "id", "amount", "category", "customer_id"]
        ],
        use_container_width=True
    )
