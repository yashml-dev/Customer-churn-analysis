import joblib


# -------------------------------------------------
# Load Saved Model
# -------------------------------------------------

MODEL_PATH = "../models/best_model.pkl"

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