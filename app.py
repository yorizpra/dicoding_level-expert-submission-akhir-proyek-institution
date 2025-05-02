import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Streamlit page config HARUS ditempatkan di awal
st.set_page_config(page_title="Jaya Jaya Institut Dropout Predictor", page_icon="🎓")

# Streamlit app title
st.title("🎓 Jaya Jaya Institut Dropout Prediction")
st.markdown("Enter student details to predict dropout risk.")

# Load model and scaler
try:
    model = joblib.load('model/model.joblib')
    scaler = joblib.load('model/scaler.joblib')

    if hasattr(model, 'feature_names_in_'):
        st.sidebar.write("Model feature names:", model.feature_names_in_.tolist())
    if hasattr(scaler, 'feature_names_in_'):
        st.sidebar.write("Scaler feature names:", scaler.feature_names_in_.tolist())
except Exception as e:
    st.error(f"Error loading model: {str(e)}")

# Add inputs for scores in the form
with st.form("student_form"):
    st.subheader("Student Information")
    gender = st.selectbox("Gender", ["female", "male"])
    race = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
    parental_edu = st.selectbox("Parental Level of Education", ["bachelor's degree", "some college", "master's degree", "associate's degree", "high school", "some high school"])
    lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
    test_prep = st.selectbox("Test Preparation Course", ["none", "completed"])
    attendance = st.number_input("Attendance (%)", min_value=0.0, max_value=100.0, value=75.0, step=0.1)
    math_score = st.number_input("Math Score", min_value=0, max_value=100, value=50)
    reading_score = st.number_input("Reading Score", min_value=0, max_value=100, value=50)
    writing_score = st.number_input("Writing Score", min_value=0, max_value=100, value=50)

    submitted = st.form_submit_button("Predict Dropout Risk")

# Prediction
if submitted:
    try:
        input_dict = {
            'gender_female': 1 if gender == 'female' else 0,
            'gender_male': 1 if gender == 'male' else 0,
            'race/ethnicity_group A': 1 if race == 'group A' else 0,
            'race/ethnicity_group B': 1 if race == 'group B' else 0,
            'race/ethnicity_group C': 1 if race == 'group C' else 0,
            'race/ethnicity_group D': 1 if race == 'group D' else 0,
            'race/ethnicity_group E': 1 if race == 'group E' else 0,
            "parental level of education_associate's degree": 1 if parental_edu == "associate's degree" else 0,
            "parental level of education_bachelor's degree": 1 if parental_edu == "bachelor's degree" else 0,
            'parental level of education_high school': 1 if parental_edu == 'high school' else 0,
            "parental level of education_master's degree": 1 if parental_edu == "master's degree" else 0,
            'parental level of education_some college': 1 if parental_edu == 'some college' else 0,
            'parental level of education_some high school': 1 if parental_edu == 'some high school' else 0,
            'lunch_free/reduced': 1 if lunch == 'free/reduced' else 0,
            'lunch_standard': 1 if lunch == 'standard' else 0,
            'test preparation course_completed': 1 if test_prep == 'completed' else 0,
            'test preparation course_none': 1 if test_prep == 'none' else 0,
            'attendance': attendance,
            'math score': math_score,
            'reading score': reading_score,
            'writing score': writing_score
        }

        input_df = pd.DataFrame([input_dict])
        input_df = input_df[scaler.feature_names_in_]  # Atur kolom agar urut dan cocok
        input_scaled = scaler.transform(input_df)

        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]

        st.subheader("Prediction Result")
        if prediction == 1:
            st.error(f"⚠️ High Dropout Risk (Probability: {probability:.2%})")
            st.markdown("**Recommendation**: Schedule counseling and provide academic support.")
        else:
            st.success(f"✅ Low Dropout Risk (Probability: {probability:.2%})")
            st.markdown("**Recommendation**: Continue monitoring performance.")

        st.subheader("Risk Probability")
        st.progress(probability)

    except Exception as e:
        st.error(f"An error occurred during prediction: {str(e)}")
        st.warning("Please ensure all input fields are filled correctly and try again.")
        st.exception(e)

# Footer
st.markdown("---")
st.markdown("Developed by Yoga Rizki Pratama | Powered by Streamlit")
