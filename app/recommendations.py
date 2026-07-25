def explain_prediction(customer, churn_probability):

    positives = []
    negatives = []

    # Contract
    if customer["Contract"].iloc[0] == "Month-to-month":
        positives.append("📄 Month-to-month contract increases churn risk.")
    else:
        negatives.append("📄 Long-term contract improves customer retention.")

    # Tenure
    if customer["tenure"].iloc[0] < 12:
        positives.append("⏳ Short customer tenure indicates a higher chance of churn.")
    elif customer["tenure"].iloc[0] > 36:
        negatives.append("⏳ Long customer tenure is a strong sign of loyalty.")

    # Monthly Charges
    if customer["MonthlyCharges"].iloc[0] > 80:
        positives.append("💷 High monthly charges may encourage customers to switch providers.")
    else:
        negatives.append("💷 Affordable monthly charges help retain customers.")

    # Tech Support
    if customer["TechSupport"].iloc[0] == "No":
        positives.append("🛠️ Customer does not have Tech Support.")
    else:
        negatives.append("🛠️ Tech Support improves customer satisfaction.")

    # Online Security
    if customer["OnlineSecurity"].iloc[0] == "No":
        positives.append("🔒 Customer does not use Online Security.")
    else:
        negatives.append("🔒 Online Security improves retention.")

    # Internet Service
    if customer["InternetService"].iloc[0] == "Fiber optic":
        positives.append("🌐 Fibre optic customers historically show higher churn.")

    # Paperless Billing
    if customer["PaperlessBilling"].iloc[0] == "Yes":
        positives.append("🧾 Paperless billing is associated with slightly higher churn.")

    return positives[:3], negatives[:3]