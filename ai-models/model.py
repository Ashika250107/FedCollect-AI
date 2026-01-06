def predict(amount, risk_level):
    if risk_level == "High":
        return "Legal Notice"
    elif risk_level == "Medium":
        return "Follow-up Call"
    else:
        return "Reminder Email"
