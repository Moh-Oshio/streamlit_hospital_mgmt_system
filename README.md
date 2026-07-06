# MRT Hospital Management System

Link to app: [[App Link](https://hospital-mgmt.streamlit.app)]

This is a hospital management system I built using Python and Streamlit. It handles patient registration, vital signs, doctor reports, and nursing notes.

## What it does
* **Role-Based Navigation:** Staff can select their department (Reception, Doctor, Nurse) to access specific tools.
* **Reception:** Create new patient cards (auto-generates a unique file number) and log vital signs.
* **Doctors:** Retrieve patient files and append medical diagnoses and prescriptions.
* **Nurses:** Append observation and care notes to patient files.
* **File-Based Database:** Uses a custom backend to store patient data securely in text files.

## Tools used
* Python & Streamlit

## How to run it locally
1. Clone the repo: `git clone https://github.com/Moh-Oshio/streamlit_hospital_mgmt_system.git`
2. Make a virtual environment: `python -m venv venv` and activate it (`venv\Scripts\activate` on Windows)
3. Install the packages: `pip install -r requirements.txt`
4. Run the app: `streamlit run Streamlit_frontend.py`
