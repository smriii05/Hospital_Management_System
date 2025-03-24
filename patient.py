from person import Person

class Patient(Person):
    def __init__(self, patient_id, name, age, gender, disease):
        super().__init__(name, age, gender)
        self.patient_id = patient_id
        self.disease = disease

    def __str__(self):
        return f"Patient ID: {self.patient_id} | {super().__str__()} | Disease: {self.disease}"