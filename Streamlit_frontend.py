import streamlit as st
from datetime import date
from Streamlit_backend import Reception, Doctor, Nurse

st.set_page_config(page_title="MRT Hospital System", layout="centered")

st.header("Hospital Management System", divider="blue")
# st.subheader(
#     "Address: No. 1 Ibrahim Hospital Road, Along Omogiafo Estate, Ibienafe, Auchi, Edo State.")

st.sidebar.title("Navigation")
with st.sidebar:
    role = st.selectbox(
        "Select Role / Department", ["Reception", "Doctor", "Nurse"])


if role == "Reception":
    st.write("### Reception Desk")
    action = st.radio("What would you like to do?", [
                      "Create New Card", "Enter Vitals", "Access Patient Card"], horizontal=True)
    staff = Reception()

    if action == "Create New Card":
        with st.form("new_patient_form", clear_on_submit=True):
            name = st.text_input("Enter patient's name")
            sex = st.selectbox("Sex", ["Male", "Female", "Other"])
            dob_date = st.date_input(
                "Date of Birth", min_value=date(1940, 1, 1), max_value="today")
            address = st.text_input("Enter address")
            phone_number = st.text_input("Enter phone number")

            if st.form_submit_button("Create Patient Record"):
                today = date.today()
                age = today.year - dob_date.year
                if (today.month, today.day) < (dob_date.month, dob_date.day):
                    age -= 1

                dob_string = dob_date.strftime("%d/%m/%Y")
                new_card_no = staff.create_card(
                    name, sex, dob_string, address, phone_number, age)
                st.success(
                    f"New card created successfully! Card Number: {new_card_no}")

    elif action == "Enter Vitals":
        with st.form("vitals_form"):
            card_no = st.text_input("Patient Card Number")
            temp = st.text_input("Temperature (°C)")
            bp = st.text_input("Blood Pressure (mmHg)")
            pulse = st.text_input("Pulse (bpm)")

            if st.form_submit_button("Save Vitals"):
                success = staff.vital_signs(card_no, temp, bp, pulse)
                if success:
                    st.success("Vital signs recorded!")
                else:
                    st.error("Patient file not found.")

    elif action == "Access Patient Card":
        card_no = st.text_input("Enter Patient's Card Number")
        if st.button("Retrieve File"):
            content = staff.check_patient_file(card_no)
            if content:
                st.text_area("Patient Record", content, height=300)
            else:
                st.error("Patient file does not exist.")


elif role == "Doctor":
    st.write("### Doctor's Portal")
    action = st.radio("What would you like to do?", [
                      "Enter Report", "Access Patient Card"], horizontal=True)
    staff = Doctor()

    if action == "Enter Report":
        with st.form("doctor_form"):
            card_no = st.text_input("Patient Card Number")
            diagnosis = st.text_area("Diagnosis")
            prescription = st.text_area("Prescription")
            notes = st.text_area("Additional Notes")

            if st.form_submit_button("Save Report"):
                success = staff.enter_report(
                    card_no, diagnosis, prescription, notes)
                if success:
                    st.success("Doctor's report saved!")
                else:
                    st.error("Patient file not found.")

    elif action == "Access Patient Card":
        card_no = st.text_input("Enter Patient's Card Number")
        if st.button("Retrieve File"):
            content = staff.check_patient_file(card_no)
            if content:
                st.text_area("Patient Record", content, height=300)
            else:
                st.error("Patient file does not exist.")


elif role == "Nurse":
    st.write("### Nurse's Station")
    action = st.radio("What would you like to do?", [
                      "Enter Notes", "Access Patient Card"], horizontal=True)
    staff = Nurse()

    if action == "Enter Notes":
        with st.form("nurse_form"):
            card_no = st.text_input("Patient Card Number")
            obs = st.text_area("Observations")
            care = st.text_area("Care given")

            if st.form_submit_button("Save Notes"):
                success = staff.enter_notes(card_no, obs, care)
                if success:
                    st.success("Nurse's notes saved!")
                else:
                    st.error("Patient file not found.")

    elif action == "Access Patient Card":
        card_no = st.text_input("Enter Patient's Card Number")
        if st.button("Retrieve File"):
            content = staff.check_patient_file(card_no)
            if content:
                st.text_area("Patient Record", content, height=300)
            else:
                st.error("Patient file does not exist.")
