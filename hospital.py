from patient import Patient
from doctor import Doctor

class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self):
        patient_id = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        age = int(input("Enter Patient Age: "))
        gender = input("Enter Patient Gender: ")
        disease = input("Enter Disease: ")
        patient = Patient(patient_id, name, age, gender, disease)
        self.patients.append(patient)
        print(f"Patient '{name}' added successfully.\n")

    def add_doctor(self):
        doctor_id = int(input("Enter Doctor ID: "))
        name = input("Enter Doctor Name: ")
        age = int(input("Enter Doctor Age: "))
        gender = input("Enter Doctor Gender: ")
        specialization = input("Enter Specialization: ")
        doctor = Doctor(doctor_id, name, age, gender, specialization)
        self.doctors.append(doctor)
        print(f"Doctor '{name}' added successfully.\n")

    def schedule_appointment(self):
        patient_id = int(input("Enter Patient ID for appointment: "))
        doctor_id = int(input("Enter Doctor ID for appointment: "))

        patient = next((p for p in self.patients if p.patient_id == patient_id), None)
        doctor = next((d for d in self.doctors if d.doctor_id == doctor_id), None)

        if patient and doctor:
            self.appointments.append((patient, doctor))
            print(f"Appointment scheduled: {patient.name} with Dr. {doctor.name} ({doctor.specialization}).\n")
        else:
            print("Invalid patient or doctor ID.\n")

    def display_patients(self):
        print("\nPatients:")
        if not self.patients:
            print("No patients found.")
        else:
            for patient in self.patients:
                print(patient)

    def display_doctors(self):
        print("\nDoctors:")
        if not self.doctors:
            print("No doctors found.")
        else:
            for doctor in self.doctors:
                print(doctor)

    def display_appointments(self):
        print("\nAppointments:")
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            for patient, doctor in self.appointments:
                print(f"{patient.name} -> Dr. {doctor.name} ({doctor.specialization})")