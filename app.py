import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("student_risk_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Student Academic Risk Prediction",
    page_icon="🎓",
    layout="wide"
)

# Title
st.title("🎓 Student Academic Performance & Risk Prediction")
st.write(
    "Enter the student's academic and personal information "
    "to predict their academic risk."
)

st.divider()

# Student input form
with st.form("student_form"):

    st.subheader("Student Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        school = st.selectbox(
            "School",
            ["GP", "MS"]
        )

        sex = st.selectbox(
            "Sex",
            ["M", "F"]
        )

        age = st.number_input(
            "Age",
            min_value=15,
            max_value=22,
            value=17
        )

        address = st.selectbox(
            "Address",
            ["U", "R"]
        )

        famsize = st.selectbox(
            "Family Size",
            ["GT3", "LE3"]
        )

        Pstatus = st.selectbox(
            "Parent Status",
            ["A", "T"]
        )

    with col2:
        Medu = st.slider(
            "Mother's Education",
            0, 4, 2
        )

        Fedu = st.slider(
            "Father's Education",
            0, 4, 2
        )

        Mjob = st.selectbox(
            "Mother's Job",
            ["teacher", "health", "services", "at_home", "other"]
        )

        Fjob = st.selectbox(
            "Father's Job",
            ["teacher", "health", "services", "at_home", "other"]
        )

        reason = st.selectbox(
            "Reason for Choosing School",
            ["course", "home", "reputation", "other"]
        )

        guardian = st.selectbox(
            "Guardian",
            ["mother", "father", "other"]
        )

    with col3:
        traveltime = st.slider(
            "Travel Time",
            1, 4, 2
        )

        studytime = st.slider(
            "Study Time",
            1, 4, 2
        )

        failures = st.slider(
            "Past Class Failures",
            0, 4, 0
        )

        absences = st.number_input(
            "Absences",
            min_value=0,
            max_value=100,
            value=5
        )

    st.subheader("Academic & Social Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        schoolsup = st.selectbox(
            "Extra School Support",
            ["yes", "no"]
        )

        famsup = st.selectbox(
            "Family Support",
            ["yes", "no"]
        )

        paid = st.selectbox(
            "Extra Paid Classes",
            ["yes", "no"]
        )

        activities = st.selectbox(
            "Extra Activities",
            ["yes", "no"]
        )

        nursery = st.selectbox(
            "Attended Nursery",
            ["yes", "no"]
        )

    with col2:
        higher = st.selectbox(
            "Wants Higher Education",
            ["yes", "no"]
        )

        internet = st.selectbox(
            "Internet Access",
            ["yes", "no"]
        )

        romantic = st.selectbox(
            "In a Romantic Relationship",
            ["yes", "no"]
        )

        famrel = st.slider(
            "Family Relationship Quality",
            1, 5, 3
        )

        freetime = st.slider(
            "Free Time",
            1, 5, 3
        )

    with col3:
        goout = st.slider(
            "Going Out",
            1, 5, 3
        )

        Dalc = st.slider(
            "Workday Alcohol Consumption",
            1, 5, 1
        )

        Walc = st.slider(
            "Weekend Alcohol Consumption",
            1, 5, 1
        )

        health = st.slider(
            "Health",
            1, 5, 3
        )

    submitted = st.form_submit_button(
        "🔍 Predict Student Risk"
    )

# Prediction
if submitted:

    student_data = {
        "school": school,
        "sex": sex,
        "age": age,
        "address": address,
        "famsize": famsize,
        "Pstatus": Pstatus,
        "Medu": Medu,
        "Fedu": Fedu,
        "Mjob": Mjob,
        "Fjob": Fjob,
        "reason": reason,
        "guardian": guardian,
        "traveltime": traveltime,
        "studytime": studytime,
        "failures": failures,
        "schoolsup": schoolsup,
        "famsup": famsup,
        "paid": paid,
        "activities": activities,
        "nursery": nursery,
        "higher": higher,
        "internet": internet,
        "romantic": romantic,
        "famrel": famrel,
        "freetime": freetime,
        "goout": goout,
        "Dalc": Dalc,
        "Walc": Walc,
        "health": health,
        "absences": absences
    }

    student_df = pd.DataFrame([student_data])

    prediction = model.predict(student_df)[0]

    probabilities = model.predict_proba(student_df)[0]

    classes = model.named_steps["model"].classes_

    risk_probability = probabilities[
        list(classes).index("At Risk")
    ]

    st.divider()

    st.subheader("Prediction Result")

    col1, col2 = st.columns(2)

    with col1:

        if prediction == "At Risk":
            st.error("⚠️ Student is At Risk")
        else:
            st.success("✅ Student is Not At Risk")

    with col2:

        st.metric(
            "At Risk Probability",
            f"{risk_probability * 100:.2f}%"
        )

    st.progress(float(risk_probability))

    if prediction == "At Risk":

        st.warning(
            "This student may require additional academic support."
        )

        st.write("### Recommended Actions")

        st.write(
            "• Monitor attendance regularly."
        )

        st.write(
            "• Provide additional academic support."
        )

        st.write(
            "• Encourage consistent study habits."
        )

        st.write(
            "• Monitor future assessment performance."
        )

    else:

        st.info(
            "The student is currently classified as Not At Risk. "
            "Continue monitoring academic performance."
        )