import streamlit as st
import joblib

model = joblib.load("decision_tree_pass_fail.pkl")

st.title("Student Pass/Fail Prediction")

study_hours = st.number_input("Study Hours", min_value=0.0, max_value=15.0)
attendance = st.number_input("Attendance (%)", min_value=0.0, max_value=100.0)

if st.button("Predict"):
    
    prediction = model.predict([[study_hours, attendance]])

    if prediction[0] == "PASS":
        st.success("Prediction: PASS")
    else:
        st.error("Prediction: FAIL")
