import json

FILE_NAME = "model_results.json"


# Create JSON file with sample model results
def create_file():
    models = [
        {
            "model_name": "Random Forest",
            "accuracy": 0.92,
            "precision": 0.90,
            "recall": 0.89,
            "f1_score": 0.895
        },
        {
            "model_name": "SVM",
            "accuracy": 0.95,
            "precision": 0.93,
            "recall": 0.92,
            "f1_score": 0.925
        },
        {
            "model_name": "Neural Network",
            "accuracy": 0.97,
            "precision": 0.96,
            "recall": 0.95,
            "f1_score": 0.955
        }
    ]

    with open(FILE_NAME, "w") as file:
        json.dump(models, file, indent=4)

    print("JSON file created successfully.")


# Read data from JSON file
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("JSON file does not exist.")
        return []


# Display all model results
def display_models():
    models = load_data()

    if not models:
        print("No model results found.")
        return

    print("\nModel Evaluation Results")
    print("-" * 80)

    for model in models:
        print("Model Name :", model["model_name"])
        print("Accuracy   :", model["accuracy"])
        print("Precision  :", model["precision"])
        print("Recall     :", model["recall"])
        print("F1-Score   :", model["f1_score"])
        print("-" * 80)


# Find model with highest accuracy and F1-score
def find_best_models():
    models = load_data()

    if not models:
        print("No model results found.")
        return

    highest_accuracy = max(models, key=lambda x: x["accuracy"])
    highest_f1 = max(models, key=lambda x: x["f1_score"])

    print("\nModel with Highest Accuracy:")
    print(highest_accuracy["model_name"])
    print("Accuracy:", highest_accuracy["accuracy"])

    print("\nModel with Highest F1-Score:")
    print(highest_f1["model_name"])
    print("F1-Score:", highest_f1["f1_score"])


# Add a new model
def add_model():
    models = load_data()

    model_name = input("Enter Model Name: ")

    # Check duplicate model
    for model in models:
        if model["model_name"].lower() == model_name.lower():
            print("Model already exists.")
            return

    accuracy = float(input("Enter Accuracy: "))
    precision = float(input("Enter Precision: "))
    recall = float(input("Enter Recall: "))
    f1_score = float(input("Enter F1-Score: "))

    new_model = {
        "model_name": model_name,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1_score
    }

    models.append(new_model)

    with open(FILE_NAME, "w") as file:
        json.dump(models, file, indent=4)

    print("New model added successfully.")


# Update an existing model
def update_model():
    models = load_data()

    model_name = input("Enter Model Name to update: ")

    found = False

    for model in models:

        if model["model_name"].lower() == model_name.lower():

            print("\nEnter new evaluation metrics:")

            model["accuracy"] = float(
                input("Enter Accuracy: ")
            )

            model["precision"] = float(
                input("Enter Precision: ")
            )

            model["recall"] = float(
                input("Enter Recall: ")
            )

            model["f1_score"] = float(
                input("Enter F1-Score: ")
            )

            found = True
            break

    if found:

        with open(FILE_NAME, "w") as file:
            json.dump(models, file, indent=4)

        print("Model updated successfully.")

    else:
        print("Model does not exist.")


# Remove a model
def remove_model():
    models = load_data()

    model_name = input("Enter Model Name to remove: ")

    found = False

    for model in models:

        if model["model_name"].lower() == model_name.lower():
            models.remove(model)
            found = True
            break

    if found:

        with open(FILE_NAME, "w") as file:
            json.dump(models, file, indent=4)

        print("Model removed successfully.")

    else:
        print("Model does not exist.")


# Main menu
def main():

    while True:

        print("\n========== ML MODEL RESULT MANAGER ==========")
        print("1. Create JSON File")
        print("2. Display Model Results")
        print("3. Find Highest Accuracy and F1-Score")
        print("4. Add New Model")
        print("5. Update Model")
        print("6. Remove Model")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()

        elif choice == "2":
            display_models()

        elif choice == "3":
            find_best_models()

        elif choice == "4":
            add_model()

        elif choice == "5":
            update_model()

        elif choice == "6":
            remove_model()

        elif choice == "7":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Try again.")


# Start program
main()