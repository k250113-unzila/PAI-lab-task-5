import csv

FILE_NAME = "patients.csv"


# Create the CSV file with sample records
def create_file():
    patients = [
        {
            "ID": "P001",
            "Age": "45",
            "BMI": "28.5",
            "BloodPressure": "130",
            "Glucose": "145",
            "Label": "Positive"
        },
        {
            "ID": "P002",
            "Age": "32",
            "BMI": "24.2",
            "BloodPressure": "118",
            "Glucose": "95",
            "Label": "Negative"
        },
        {
            "ID": "P003",
            "Age": "55",
            "BMI": "31.8",
            "BloodPressure": "140",
            "Glucose": "180",
            "Label": "Positive"
        }
    ]

    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = [
            "ID", "Age", "BMI",
            "BloodPressure", "Glucose", "Label"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(patients)

    print("CSV file created successfully.")


# Display all patient records
def display_records():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            print("\nPatient Records")
            print("-" * 80)

            for patient in reader:
                print(
                    "ID:", patient["ID"],
                    "| Age:", patient["Age"],
                    "| BMI:", patient["BMI"],
                    "| BP:", patient["BloodPressure"],
                    "| Glucose:", patient["Glucose"],
                    "| Label:", patient["Label"]
                )

            print("-" * 80)

    except FileNotFoundError:
        print("File does not exist. Create the file first.")


# Count positive and negative cases
def count_cases():
    try:
        positive = 0
        negative = 0

        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for patient in reader:
                if patient["Label"].lower() == "positive":
                    positive += 1

                elif patient["Label"].lower() == "negative":
                    negative += 1

        print("\nPositive cases:", positive)
        print("Negative cases:", negative)

    except FileNotFoundError:
        print("File does not exist.")


# Find patients with glucose above a threshold
def high_glucose():
    try:
        threshold = float(input("Enter glucose threshold: "))

        found = False

        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            print("\nPatients with high glucose:")

            for patient in reader:
                glucose = float(patient["Glucose"])

                if glucose > threshold:
                    print(
                        "ID:", patient["ID"],
                        "| Glucose:", patient["Glucose"]
                    )
                    found = True

        if not found:
            print("No patient found above this threshold.")

    except FileNotFoundError:
        print("File does not exist.")


# Calculate average BMI and glucose
def calculate_average():
    try:
        total_bmi = 0
        total_glucose = 0
        count = 0

        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for patient in reader:
                total_bmi += float(patient["BMI"])
                total_glucose += float(patient["Glucose"])
                count += 1

        if count == 0:
            print("No records available.")
            return

        average_bmi = total_bmi / count
        average_glucose = total_glucose / count

        print("\nAverage BMI:", round(average_bmi, 2))
        print("Average Glucose:", round(average_glucose, 2))

    except FileNotFoundError:
        print("File does not exist.")


# Add a new patient
def add_patient():
    try:
        patient_id = input("Enter Patient ID: ")

        # Check for duplicate ID
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for patient in reader:
                if patient["ID"] == patient_id:
                    print("Patient ID already exists.")
                    return

        age = input("Enter Age: ")
        bmi = input("Enter BMI: ")
        bp = input("Enter Blood Pressure: ")
        glucose = input("Enter Glucose Level: ")
        label = input("Enter Diabetes Label (Positive/Negative): ")

        new_patient = {
            "ID": patient_id,
            "Age": age,
            "BMI": bmi,
            "BloodPressure": bp,
            "Glucose": glucose,
            "Label": label
        }

        with open(FILE_NAME, "a", newline="") as file:
            fieldnames = [
                "ID", "Age", "BMI",
                "BloodPressure", "Glucose", "Label"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(new_patient)

        print("New patient added successfully.")

    except FileNotFoundError:
        print("File does not exist.")


# Update an existing patient
def update_patient():
    patient_id = input("Enter Patient ID to update: ")

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            patients = list(reader)

        found = False

        for patient in patients:
            if patient["ID"] == patient_id:
                print("\nEnter new information:")

                patient["Age"] = input("Enter Age: ")
                patient["BMI"] = input("Enter BMI: ")
                patient["BloodPressure"] = input("Enter Blood Pressure: ")
                patient["Glucose"] = input("Enter Glucose Level: ")
                patient["Label"] = input("Enter Diabetes Label (Positive/Negative): ")

                found = True
                break

        if found:
            with open(FILE_NAME, "w", newline="") as file:
                fieldnames = [
                    "ID", "Age", "BMI",
                    "BloodPressure", "Glucose", "Label"
                ]

                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(patients)

            print("Patient record updated successfully.")

        else:
            print("Patient ID does not exist.")

    except FileNotFoundError:
        print("File does not exist.")


# Main menu
def main():
    while True:
        print("\n========== PATIENT DATA MANAGER ==========")
        print("1. Create CSV File")
        print("2. Display Records")
        print("3. Count Positive/Negative Cases")
        print("4. Find High Glucose Patients")
        print("5. Calculate Average BMI and Glucose")
        print("6. Add New Patient")
        print("7. Update Patient")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            display_records()
        elif choice == "3":
            count_cases()
        elif choice == "4":
            high_glucose()
        elif choice == "5":
            calculate_average()
        elif choice == "6":
            add_patient()
        elif choice == "7":
            update_patient()
        elif choice == "8":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Try again.")


# Run the program
if __name__ == "__main__":
    main()
