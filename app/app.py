import streamlit as st
import pandas as pd
import predict
import plotly.express as px
from report_generator import generate_pdf

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
    padding: clamp(12px, 2vw, 18px);
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
    font-size:clamp(14px, 2vw, 16px);
    font-weight:600;
}

/* Metric Value */

[data-testid="stMetricValue"]{
    font-size:clamp(26px, 4vw, 32px);
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
    st.divider()
    st.subheader("🎯 Model Confidence")
    confidence = abs(churn_probability - 50) * 2

    if confidence >= 80:
        confidence_level = "🟢 High"
    elif confidence >= 50:
        confidence_level = "🟡 Moderate"
    else:
        confidence_level = "🔴 Low"
    left, right = st.columns([1, 3])
    with left:
        st.metric("Confidence", f"{confidence:.1f}% ")
    with right:
        st.markdown(f"### {confidence_level} Confidence")
    st.progress(confidence / 100)
    if confidence >= 80:
        st.success(
            "The model is highly confident in this prediction because the customer's profile strongly matches historical churn patterns."
        )

    elif confidence >= 50:
        st.info(
            "The model has moderate confidence. Some customer characteristics indicate churn, while others suggest the customer may stay."
        )

    else:
        st.warning(
            "The prediction is close to the decision boundary. The customer exhibits a mix of churn and retention characteristics, so this prediction should be interpreted with caution."
        )


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
    # Dictionary to store feature impact scores
    feature_scores = {}

    if contract == "Month-to-month":
        risk_factors.append("📄 Month-to-month contract generally has a higher churn rate.")
        feature_scores["Month-to-month Contract"] = 5
    else:
        positive_factors.append("📄 Long-term contract improves customer retention.")
        feature_scores["Long-term Contract"] = -5
    # Tenure
    if tenure < 12:
        risk_factors.append("⏳ Customer has a short tenure.")
        feature_scores["Short Tenure"] = 4
    elif tenure > 36:
        positive_factors.append("⏳ Long customer tenure indicates loyalty.")
        feature_scores["Long Tenure"] = -4
    # Monthly Charges
    if monthly > 80:
        risk_factors.append("💷 High monthly charges may increase churn risk.")
        feature_scores["High Monthly Charges"] = 3
    else:
        positive_factors.append("💷 Affordable monthly charges improve retention.")
        feature_scores["Affordable Charges"] = -3
    # Tech Support
    if tech_support == "No":
        risk_factors.append("🛠 Customer does not have Tech Support.")
        feature_scores["No Tech Support"] = 3
    else:
        positive_factors.append("🛠 Customer has Tech Support.")
        feature_scores["Tech Support"] = -3
    # Online Security
    if online_security == "No":
        risk_factors.append("🔒 Customer does not use Online Security.")
        feature_scores["No Online Security"] = 4
    else:
        positive_factors.append("🔒 Online Security helps retain customers.")
        feature_scores["Online Security"] = -4
    # Internet Service
    if internet_service == "Fiber optic":
        risk_factors.append("🌐 Fibre optic customers historically show higher churn.")
        feature_scores["Fiber Optic"] = 2
    # Paperless Billing
    if paperless_billing == "Yes":
        risk_factors.append("🧾 Paperless billing is associated with slightly higher churn.")
        feature_scores["Paperless Billing"] = 2
    # -------------------------
    # Feature Impact Analysis
    # ------------------------- 
    impact_df = pd.DataFrame(
        list(feature_scores.items()),
        columns = ["Feature", "Impact"]
    )

    impact_df = impact_df.sort_values("Impact")
    

    fig = px.bar(
        impact_df,
        x="Impact",
        y="Feature",
        orientation="h",
        color="Impact",
        color_continuous_scale=["#2ECC71", "#F1C40F", "#E74C3C"]
    )

    fig.update_layout(
        
        height=350,
        template="plotly_dark",
        xaxis_title="",
        yaxis_title="",
        xaxis = dict(
            showticklabels=False,
            showgrid=False,
            zeroline=True,
            zerolinecolor="gray"

        ),
        coloraxis_showscale=False,
        margin=dict(l=20, r=20, t=60, b=20),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )
    fig.update_traces(
        hovertemplate="<b>%{y}</b><br>Impact Score: %{x}<extra></extra>",
        width = 0.55
    )
    st.plotly_chart(fig, use_container_width=True)
    st.caption(
        "Positive values indicate factors associated with higher churn risk, while negative values indicate factors associated with customer retention."
    )
    st.caption(
        "The chart visualizes rule-based factors contributing to the prediction and is intended to aid interpretation."
    )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.markdown("### ⚠️ Churn Risk Factors")

        if risk_factors:
            for factor in risk_factors[:4]:
                st.warning(factor)
        else:
            st.success("No major churn risk factors detected.")
        st.divider()
        st.subheader("💡Recommended Actions")
        
        if churn_probability >= 70:
            recommendations = [
                "🎁 Offer a loyalty discount",
                "👨‍💼 Assign a dedicated support executive",
                "📄 Recommend a long-term contract",
                "📞 Contact the customer immediately"

            ]
            for recommendation in recommendations:
                st.error(recommendation)
        
            
        
        elif churn_probability >= 40:
        
            recommendations = [
                "📧 Send personalised offers",
                "🎁 Recommend value-added services",
                "📊 Monitor customer activity"
            ]
            for recommendation in recommendations:
                st.warning(recommendation)
        
        else:
        
            recommendations = [
                "😊 Customer appears satisfied",
                "🤝 Continue regular engagement",
                "⭐ Promote premium plans when appropriate"
            ]
            for recommendation in recommendations:
                st.success(recommendation)

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

            business_insight = f"""
                This customer has a **HIGH predicted churn risk ({churn_probability:.2f}%)**.

                The customer's profile indicates multiple characteristics commonly associated
                with churn, such as a short-term contract, limited retention services, or
                higher monthly charges.

                **Suggested business action:**

                • Contact the customer proactively.

                • Offer a long-term contract with incentives.

                • Promote value-added services to improve customer satisfaction.
                """
            st.info(business_insight)

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
        report_data = {

        # Prediction
            "prediction": prediction,
            "risk_level": risk,
            "churn_probability": churn_probability,
            "stay_probability": stay_probability,

    # Customer Details
            "gender": gender,
            "senior_citizen": senior,
            "partner": partner,
            "dependents": dependents,

            "tenure": tenure,
            "contract": contract,
            "internet_service": internet_service,
            "tech_support": tech_support,

            "monthly_charges": monthly,
            "total_charges": total,

    # Analysis
            "risk_factors": risk_factors,
            "positive_factors": positive_factors,
            "feature_scores": feature_scores,

    # Text Sections
            "business_insight": business_insight,
            "recommendations": recommendations
        }
        pdf = generate_pdf(report_data)
        st.download_button(
            label = "📄 Download Customer Churn Analysis Report",
            data=pdf,
            file_name="Customer_Churn_Report.pdf",
            mime="application/pdf"
        )