import streamlit as st

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

st.divider()

predict = st.button(
    "🚀 Predict Customer Churn",
    use_container_width=True
)