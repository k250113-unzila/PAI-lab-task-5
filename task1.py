FILE_NAME = "experiments.txt"


# Create file and store initial experiments
def create_file():
    experiments = [
        ["E001", "CNN", "CIFAR10", "0.001", "20"],
        ["E002", "LSTM", "IMDB", "0.0005", "30"],
        ["E003", "RandomForest", "Iris", "0.01", "50"]
    ]

    with open(FILE_NAME, "w") as file:
        for exp in experiments:
            file.write(",".join(exp) + "\n")

    print("File created and experiments stored successfully.")


# Read and display all experiments
def display_experiments():
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No experiments found.")
            return

        print("\nExperiment Configurations:")
        print("-" * 70)
        print(f"{'ID':<10}{'Model':<15}{'Dataset':<15}{'LR':<12}{'Epochs':<10}")
        print("-" * 70)

        for line in lines:
            data = line.strip().split(",")

            if len(data) == 5:
                print(f"{data[0]:<10}{data[1]:<15}{data[2]:<15}"
                      f"{data[3]:<12}{data[4]:<10}")

        print("-" * 70)

    except FileNotFoundError:
        print("File does not exist. Please create the file first.")


# Search for an experiment by ID
def search_experiment():
    search_id = input("Enter Experiment ID to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")

                if data[0] == search_id:
                    print("\nExperiment Found:")
                    print("Experiment ID :", data[0])
                    print("Model Name    :", data[1])
                    print("Dataset Name  :", data[2])
                    print("Learning Rate :", data[3])
                    print("Epochs        :", data[4])
                    return

        print("Experiment with this ID does not exist.")

    except FileNotFoundError:
        print("File does not exist.")


# Add a new experiment
def add_experiment():
    exp_id = input("Enter Experiment ID: ")

    # Check if ID already exists
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")

                if data[0] == exp_id:
                    print("Experiment ID already exists.")
                    return

    except FileNotFoundError:
        pass

    model = input("Enter Model Name: ")
    dataset = input("Enter Dataset Name: ")
    learning_rate = input("Enter Learning Rate: ")
    epochs = input("Enter Number of Epochs: ")

    with open(FILE_NAME, "a") as file:
        file.write(
            f"{exp_id},{model},{dataset},{learning_rate},{epochs}\n"
        )

    print("New experiment added successfully.")


# Update an existing experiment
def update_experiment():
    update_id = input("Enter Experiment ID to update: ")

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        found = False

        for i in range(len(lines)):
            data = lines[i].strip().split(",")

            if data[0] == update_id:
                print("\nEnter new values:")

                model = input("Enter Model Name: ")
                dataset = input("Enter Dataset Name: ")
                learning_rate = input("Enter Learning Rate: ")
                epochs = input("Enter Number of Epochs: ")

                lines[i] = (
                    f"{update_id},{model},{dataset},"
                    f"{learning_rate},{epochs}\n"
                )

                found = True
                break

        if found:
            with open(FILE_NAME, "w") as file:
                file.writelines(lines)

            print("Experiment updated successfully.")
        else:
            print("Experiment with this ID does not exist.")

    except FileNotFoundError:
        print("File does not exist.")


# Delete an experiment
def delete_experiment():
    delete_id = input("Enter Experiment ID to remove: ")

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        new_lines = []
        found = False

        for line in lines:
            data = line.strip().split(",")

            if data[0] == delete_id:
                found = True
            else:
                new_lines.append(line)

        if found:
            with open(FILE_NAME, "w") as file:
                file.writelines(new_lines)

            print("Experiment removed successfully.")
        else:
            print("Experiment with this ID does not exist.")

    except FileNotFoundError:
        print("File does not exist.")


# Main menu
def main():
    while True:
        print("\n========== AI EXPERIMENT MANAGER ==========")
        print("1. Create File")
        print("2. Display Experiments")
        print("3. Search Experiment")
        print("4. Add Experiment")
        print("5. Update Experiment")
        print("6. Remove Experiment")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()

        elif choice == "2":
            display_experiments()

        elif choice == "3":
            search_experiment()

        elif choice == "4":
            add_experiment()

        elif choice == "5":
            update_experiment()

        elif choice == "6":
            delete_experiment()

        elif choice == "7":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please try again.")


# Start program
main()