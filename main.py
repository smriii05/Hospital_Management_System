from hospital import Hospital
from patient import Patient
from doctor import Doctor

def main():
    hospital = Hospital("City Hospital")

    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Schedule Appointment")
        print("4. Display Patients")
        print("5. Display Doctors")
        print("6. Display Appointments")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hospital.add_patient()
        elif choice == "2":
            hospital.add_doctor()
        elif choice == "3":
            hospital.schedule_appointment()
        elif choice == "4":
            hospital.display_patients()
        elif choice == "5":
            hospital.display_doctors()
        elif choice == "6":
            hospital.display_appointments()
        elif choice == "7":
            print("Exiting system....")
            break
        else:
            print("Invalid choice! Please enter a valid option.")


if __name__ == "__main__":
    main()
