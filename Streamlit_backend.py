import bcrypt
import os
from random import randint
from datetime import datetime

card_nums = []


class HospitalStaff:
    def __init__(self):
        self.folder = "patients"
        os.makedirs(self.folder, exist_ok=True)

    def check_patient_file(self, card_number):
        file_path = os.path.join(self.folder, f"{card_number}.txt")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                return file.read()
        return None


class Reception(HospitalStaff):
    def __init__(self):
        super().__init__()
        try:
            with open("file_numbers.txt", "r") as file:
                for line in file:
                    number = line.strip()
                    if number and number not in card_nums:
                        card_nums.append(number)
        except FileNotFoundError:
            pass

    def create_card(self, name: str, sex: str, dob: str, address: str, phone_no: str, age) -> str:
        while True:
            rand_num = str(randint(100, 5000))
            def_len = 6
            file_no = ((def_len - len(rand_num)) * "0") + rand_num
            if file_no not in card_nums:
                break

        card_nums.append(file_no)
        with open("file_numbers.txt", "a") as file:
            file.write(f"{file_no}\n")

        file_path = os.path.join(self.folder, f"{file_no}.txt")
        with open(file_path, "a") as file:
            file.write(
                f"--- PATIENT CARD CREATED ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---\n")
            file.write(f"File Number: {file_no}\n")
            file.write(f"Name of Patient: {name}\n")
            file.write(f"Sex: {sex}\n")
            file.write(f"Age: {age} years\n")
            file.write(f"Address: {address}\n")
            file.write(f"Phone: {phone_no}\n")

        return file_no

    def vital_signs(self, card_no: str, temp: str, bp: str, pulse: str) -> bool:
        file_path = os.path.join(self.folder, f"{card_no}.txt")
        if not os.path.exists(file_path):
            return False

        with open(file_path, "a") as file:
            file.write(
                f"\n--- VITAL SIGNS ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---\n")
            file.write(f"Temperature: {temp}°C\n")
            file.write(f"Blood Pressure: {bp}mmHg\n")
            file.write(f"Pulse: {pulse} bpm\n")
        return True


class Doctor(HospitalStaff):
    def enter_report(self, card_no: str, diagnosis: str, prescription: str, notes: str) -> bool:
        file_path = os.path.join(self.folder, f"{card_no}.txt")
        if not os.path.exists(file_path):
            return False

        with open(file_path, "a") as file:
            file.write(
                f"\n--- DOCTOR'S REPORT ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---\n")
            file.write(f"Diagnosis: {diagnosis}\n")
            file.write(f"Prescription: {prescription}\n")
            file.write(f"Notes: {notes}\n")
        return True


class Nurse(HospitalStaff):
    def enter_notes(self, card_no: str, observations: str, care: str) -> bool:
        file_path = os.path.join(self.folder, f"{card_no}.txt")
        if not os.path.exists(file_path):
            return False

        with open(file_path, "a") as file:
            file.write(
                f"\n--- NURSE'S NOTES ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---\n")
            file.write(f"Observations: {observations}\n")
            file.write(f"Care: {care}\n")
        return True
