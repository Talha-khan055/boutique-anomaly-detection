
import pandas as pd
import numpy as np
import pickle
from pathlib import Path
from sklearn.ensemble import IsolationForest
from sklearn.metrics import precision_score

# File paths
DATA_PATH = Path("data/transactions.csv")
MODEL_PATH = Path("model.pkl")

# Load transaction data
df = pd.read_csv(DATA_PATH)

# Create synthetic anomaly labels (approximately 5%)
if "is_anomaly" not in df.columns:
    rng = np.random.default_rng(42)
    df["is_anomaly"] = False

    anomaly_count = round(len(df) * 0.05)
    anomaly_indices = rng.choice(
        df.index,
        size=anomaly_count,
        replace=False
    )

    df.loc[anomaly_indices, "is_anomaly"] = True
    df.to_csv(DATA_PATH, index=False)

print("Synthetic anomaly labels created.")

# Select numeric features
features = ["amount"]
X = df[features]

# Train Isolation Forest
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

model.fit(X)

# Predict anomalies (-1 means anomaly, 1 means normal)
predictions = model.predict(X)
predicted_anomalies = (predictions == -1)

# Evaluate precision using synthetic labels
precision = precision_score(
    df["is_anomaly"],
    predicted_anomalies,
    zero_division=0
)

print("\nModel Evaluation")
print("----------------")
print("Total transactions:", len(df))
print("Synthetic anomalies:", int(df["is_anomaly"].sum()))
print("Predicted anomalies:", int(predicted_anomalies.sum()))
print("Precision:", round(precision, 4))

# Save trained model
with open(MODEL_PATH, "wb") as file:
    pickle.dump(model, file)

print("\nModel successfully saved as model.pkl")
