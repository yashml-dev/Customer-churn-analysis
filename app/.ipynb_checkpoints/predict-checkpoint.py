import joblib


# -------------------------------------------------
# Load Saved Model
# -------------------------------------------------

MODEL_PATH = "../models/best_model.pkl"

model = joblib.load(MODEL_PATH)


# -------------------------------------------------
# Prediction Function
# -------------------------------------------------

def predict_customer(customer_df):

    prediction = model.predict(customer_df)[0]

    probability = model.predict_proba(customer_df)[0]

    return prediction, probability