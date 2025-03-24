from person import Person

class Doctor(Person):
    def __init__(self, doctor_id, name, age, gender, specialization):
        super().__init__(name, age, gender)
        self.doctor_id = doctor_id
        self.specialization = specialization

    def __str__(self):
        return f"Doctor ID: {self.doctor_id} | {super().__str__()} | Specialization: {self.specialization}"
