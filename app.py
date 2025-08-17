import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load trained model
with open("student_performance_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="🎓 Student Performance Predictor", layout="centered")

st.title("🎓 Student Performance Predictor")
st.write("Enter the student details to predict whether they are likely to **Pass or Fail**.")

# Input form
with st.form("student_form"):
    study_hours = st.number_input("Study Hours per Week", min_value=0, max_value=60, value=20)
    attendance = st.slider("Attendance Rate (%)", min_value=0, max_value=100, value=80)
    prev_grades = st.slider("Previous Grades (0–100)", min_value=0, max_value=100, value=70)
    extracurricular = st.radio("Participation in Extracurricular Activities", ["Yes", "No"])
    parent_edu = st.selectbox("Parent Education Level", ["High School", "Bachelor", "Master", "Doctorate"])

    submitted = st.form_submit_button("Predict")

if submitted:
    # Convert inputs into DataFrame (same structure as training data)
    input_data = pd.DataFrame({
        "Study Hours per Week": [study_hours],
        "Attendance Rate": [attendance],
        "Previous Grades": [prev_grades],
        "Participation in Extracurricular Activities": [1 if extracurricular=="Yes" else 0],
        "Parent Education Level": [parent_edu]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Show result
    if prediction == 1:
        st.success(f"✅ The student is likely to PASS ")
    else:
        st.error(f"❌ The student is likely to FAIL ")
