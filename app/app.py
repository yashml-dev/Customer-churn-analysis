import streamlit as st
import pandas as pd
import predict

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
st.markdown("""
<style>

/* ---------- Metric Cards ---------- */

[data-testid="stMetric"]{
    background-color: #1E1E1E;
    border: 1px solid #2E2E2E;
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
}

/* Hover Effect */

[data-testid="stMetric"]:hover{
    border: 1px solid #4A90E2;
    transform: translateY(-2px);
    transition: 0.25s;
}

/* Metric Label */

[data-testid="stMetricLabel"]{
    font-size:16px;
    font-weight:600;
}

/* Metric Value */

[data-testid="stMetricValue"]{
    font-size:32px;
    font-weight:700;
}

/* Progress Bar */

.stProgress > div > div > div > div{
    background-color:#4A90E2;
}

</style>
""", unsafe_allow_html=True)
def profile_card(title, data):
    st.markdown(f"### {title}")

    for key, value in data.items():
        left, right = st.columns([2, 2])

        with left:
            st.markdown(f"**{key}**")

        with right:
            st.write(value)

    st.divider()


# ============================
# Sidebar
# ============================

with st.sidebar:

    st.title("📊 Customer Churn")

    st.markdown("---")

    st.subheader("Project Information")

    st.write("""
    Predict whether a telecom customer is likely to churn
    using a trained Machine Learning model.
    """)

    st.markdown("---")

    st.subheader("Model")

    st.success("Logistic Regression")

    st.write("Accuracy : **81%**")
    st.write("ROC-AUC : **0.85**")

    st.markdown("---")

    st.subheader("Dataset")

    st.write("IBM Telco Customer Churn")

    st.markdown("---")

    st.subheader("Technologies")

    st.write("""
    ✅ Python

    ✅ Streamlit

    ✅ Scikit-Learn

    ✅ Pandas

    ✅ Power BI
    """)

    st.markdown("---")

    st.caption("Made by Yash Malviya")
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
    "🚀 Analyse Churn Risk",
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
    

    prediction, probability = predict_customer(customer_data)

    churn_probability = probability[1] * 100
    stay_probability = probability[0] * 100
    st.divider()

    st.subheader("📊 Prediction overview")
    st.divider()
    card1, card2, card3, card4 = st.columns(4)

    with card1:

        st.metric(
            "Prediction",
            "Likely to Churn" if prediction else "Likely to Stay"
    )

    with card2:

        st.metric(
            "Stay Probability",
            f"{stay_probability:.2f}%"
        )

    with card3:

        st.metric(
            "Churn Probability",
            f"{churn_probability:.2f}%"
        )

    with card4:

        if churn_probability >= 70:
            risk = "🔴 HIGH"

        elif churn_probability >= 40:
            risk = "🟡 MEDIUM"

        else:
            risk = "🟢 LOW"

        st.metric(
            "Risk Level",
            risk
        )

    st.markdown("### Churn Probability")

    st.progress(churn_probability / 100)
# -------------------------
# Customer Summary
# -------------------------
    
    st.subheader("👤 Customer Profile")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        profile_card(
            "👤 Personal Information",
            {
                "Gender": gender,
                "Senior Citizen": senior,
                "Partner": partner,
                "Dependents": dependents
            }
        )

    with col2:

        profile_card(
            "📞 Services & Contract",
            {
                "Phone Service": phone_service,
                "Internet": internet_service,
                "Contract": contract,
                "Tech Support": tech_support
            }
        )

    with col3:

        profile_card(
            "💳 Billing Information",
            {
                "Monthly Charges": f"${monthly:.2f}",
                "Total Charges": f"${total:.2f}",
                "Payment Method": payment_method,
                "Paperless Billing": paperless_billing
            }
        )
# -------------------------
# Retention Recommendation
# -------------------------

    

    st.subheader("🔍 Key Factors Influencing the Prediction")

    risk_factors = []
    positive_factors = []

    if contract == "Month-to-month":
        risk_factors.append("📄 Month-to-month contract generally has a higher churn rate.")
    else:
        positive_factors.append("📄 Long-term contract improves customer retention.")
    # Tenure
    if tenure < 12:
        risk_factors.append("⏳ Customer has a short tenure.")
    elif tenure > 36:
        positive_factors.append("⏳ Long customer tenure indicates loyalty.")
    # Monthly Charges
    if monthly > 80:
        risk_factors.append("💷 High monthly charges may increase churn risk.")
    else:
        positive_factors.append("💷 Affordable monthly charges improve retention.")
    # Tech Support
    if tech_support == "No":
        risk_factors.append("🛠 Customer does not have Tech Support.")
    else:
        positive_factors.append("🛠 Customer has Tech Support.")
    # Online Security
    if online_security == "No":
        risk_factors.append("🔒 Customer does not use Online Security.")
    else:
        positive_factors.append("🔒 Online Security helps retain customers.")
    # Internet Service
    if internet_service == "Fiber optic":
        risk_factors.append("🌐 Fibre optic customers historically show higher churn.")
    # Paperless Billing
    if paperless_billing == "Yes":
        risk_factors.append("🧾 Paperless billing is associated with slightly higher churn.")
    left, right = st.columns(2)

    with left:

        st.markdown("### ⚠️ Churn Risk Factors")

        if risk_factors:
            for factor in risk_factors[:4]:
                st.warning(factor)
        else:
            st.success("No major churn risk factors detected.")
        st.divider()
        st.subheader("💡 Retention Recommendation")
        
        if churn_probability >= 70:
        
            st.error("🎁 Offer a loyalty discount")
            st.error("👨‍💼 Assign a dedicated support executive")
            st.error("📄 Recommend a long-term contract")
            st.error("📞 Contact the customer immediately")
        
        elif churn_probability >= 40:
        
            st.warning("""
                • Send personalised offers
        
                • Recommend value-added services
        
                • Monitor customer activity
                    """)
        
        else:
        
            st.success("""
                • Customer appears satisfied
    
                • Continue regular engagement
        
                •    Promote premium plans when appropriate
                    """)

    with right:

        st.markdown("### ✅ Positive Factors")

        if positive_factors:
            for factor in positive_factors[:4]:
             st.success(factor)
        else:
            st.info("No strong retention factors detected.")
        
        st.divider()

        st.subheader("📈 Business Insight")

        if churn_probability >= 70:

            st.info(f"""
                This customer has a **HIGH predicted churn risk ({churn_probability:.2f}%)**.

                The customer's profile indicates multiple characteristics commonly associated
                with churn, such as a short-term contract, limited retention services, or
                higher monthly charges.

                **Suggested business action:**

                • Contact the customer proactively.

                • Offer a long-term contract with incentives.

                • Promote value-added services to improve customer satisfaction.
                """)

        elif churn_probability >= 40:

            st.info(f"""
                This customer has a **MODERATE predicted churn risk ({churn_probability:.2f}%)**.

                While there are no immediate signs of churn, some attributes indicate
                that the customer may consider switching providers in the future.

                **Suggested business action:**

                • Send personalised offers.

                • Recommend bundled services.

                • Continue monitoring customer engagement.
            """)

        else:

            st.info(f"""
                This customer has a **LOW predicted churn risk ({churn_probability:.2f}%)**.

                The customer's profile reflects strong loyalty and continued engagement
                with the company's services.

                **Suggested business action:**

                • Focus on cross-selling premium services.

                • Maintain regular engagement and customer satisfaction.
            """)