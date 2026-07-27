import joblib
from pathlib import Path
import os

# -------------------------------------------------
# Load Saved Model
# -------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "best_model.pkl"

print("Current working directory:", os.getcwd())
print("BASE_DIR:", BASE_DIR)
print("MODEL_PATH:", MODEL_PATH)
print("Exists?", MODEL_PATH.exists())

model = joblib.load(MODEL_PATH)
print(model)


# -------------------------------------------------
# Prediction Function
# -------------------------------------------------

def predict_customer(customer_df):
    """
    Predict whether a customer will churn.
    """


    prediction = model.predict(customer_df)[0]

    probability = model.predict_proba(customer_df)[0]

    return prediction, probability
def get_model():
    print("get_model exists")
    return model
print("predict.py loaded")