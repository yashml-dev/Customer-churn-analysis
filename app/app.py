import streamlit as st
import pandas as pd
from predict import predict_customer



# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Customer Churn Intelligence Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------
# Main Title
# -------------------------------------------------
st.title("📊 Customer Churn Intelligence Dashboard")

st.markdown(
    "Predict customer churn and generate actionable retention insights."
)

# =====================================================
# Customer Information Form
# =====================================================

st.header("📝 Customer Information")

col1, col2 = st.columns(2)

with col1:

    st.subheader("👤 Personal Information")

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )
    st.subheader("📞 Phone Services")

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    if phone_service == "Yes":
        multiple_lines = st.selectbox(
            "Multiple Lines",
            ["Yes", "No"]
        )
    else:
        multiple_lines = "No phone service"

with col2:

    st.subheader("📈 Account Information")

    tenure = st.slider(
        "Tenure (Months)",
        min_value=0,
        max_value=72,
        value=12
    )

    monthly = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    total = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=840.0
    )
    st.subheader("🌐 Internet Services")

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )   

    if internet_service != "No":

        online_security = st.selectbox(
            "Online Security",
            ["Yes", "No"]
        )

        online_backup = st.selectbox(
            "Online Backup",
            ["Yes", "No"]
        )

        device_protection = st.selectbox(
            "Device Protection",
            ["Yes", "No"]
        )

        tech_support = st.selectbox(
            "Tech Support",
            ["Yes", "No"]
        )

        streaming_tv = st.selectbox(
            "Streaming TV",
            ["Yes", "No"]
        )

        streaming_movies = st.selectbox(
            "Streaming Movies",
            ["Yes", "No"]
        )

    else:

        online_security = "No internet service"
        online_backup = "No internet service"
        device_protection = "No internet service"
        tech_support = "No internet service"
        streaming_tv = "No internet service"
        streaming_movies = "No internet service"
    st.subheader("💳 Contract & Billing")

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        [
            "Yes",
            "No"
        ]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

st.divider()

predict = st.button(
    "🚀 Predict Customer Churn",
    use_container_width=True
)
if predict:

    customer_data = pd.DataFrame({

        "gender": [gender],
        "SeniorCitizen": [senior],          # Yes / No
        "Partner": [partner],
        "Dependents": [dependents],

        "tenure": [tenure],

        "PhoneService": [phone_service],
        "MultipleLines": [multiple_lines],

        "InternetService": [internet_service],
        "OnlineSecurity": [online_security],
        "OnlineBackup": [online_backup],
        "DeviceProtection": [device_protection],
        "TechSupport": [tech_support],
        "StreamingTV": [streaming_tv],
        "StreamingMovies": [streaming_movies],

        "Contract": [contract],
        "PaperlessBilling": [paperless_billing],
        "PaymentMethod": [payment_method],

        "MonthlyCharges": [monthly],
        "TotalCharges": [total]

    })
    st.write(customer_data)

    prediction, probability = predict_customer(customer_data)

    churn_probability = probability[1] * 100

    col1, col2 = st.columns(2)

    with col1:

        if prediction == 1:
            st.error("⚠️ High Risk of Churn")
        else:
            st.success("✅ Customer Likely to Stay")

    with col2:

        st.metric(
            "Churn Probability",
            f"{churn_probability:.2f}%"
        )
    if churn_probability >= 70:
        st.error("🔴 Risk Level: HIGH")

    elif churn_probability >= 40:
        st.warning("🟡 Risk Level: MEDIUM")

    else:
        st.success("🟢 Risk Level: LOW")
    st.subheader("💡 Retention Recommendation")
    if churn_probability >= 70:

        st.write("""
        • Offer a loyalty discount.
        • Assign a customer support executive.
        • Recommend a long-term contract.
        • Contact the customer immediately.
        """)

    elif churn_probability >= 40:

        st.write("""
        • Send personalized offers.
        • Recommend value-added services.
        • Monitor customer activity.
        """)

    else:

        st.write("""
        • Customer appears satisfied.
        • Continue regular engagement.
        • Offer premium plans when appropriate.
        """)