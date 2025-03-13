

# Define a dictionary of diseases, their symptoms, and severity levels
diseases = {
    "Common Cold": {
        "symptoms": ["cough", "sore throat", "runny nose", "sneezing"],
        "severity": "Mild"
    },
    "Flu": {
        "symptoms": ["fever", "cough", "headache", "muscle pain", "fatigue"],
        "severity": "Moderate"
    },
    "COVID-19": {
        "symptoms": ["fever", "cough", "shortness of breath", "loss of taste or smell"],
        "severity": "High"
    },
    "Allergy": {
        "symptoms": ["sneezing", "itchy eyes", "runny nose", "rash"],
        "severity": "Mild"
    },
    "Migraine": {
        "symptoms": ["headache", "nausea", "sensitivity to light"],
        "severity": "Moderate"
    }
}

# List of common symptoms for the user to choose from
common_symptoms = [
    "cough", "fever", "headache", "sore throat", "runny nose", "sneezing",
    "muscle pain", "fatigue", "shortness of breath", "loss of taste or smell",
    "itchy eyes", "rash", "nausea", "sensitivity to light"
]

# Symptom history to store user's previous diagnoses
symptom_history = []

# Function to display the welcome message and menu
def display_menu():
    print("\n==============================================")
    print("  Welcome to the AI-Powered Medical Diagnosis System!")
    print("==============================================")
    print("Please choose an option:")
    print("1. Check your symptoms")
    print("2. View symptom history")
    print("3. Get health tips")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ").strip()
    return choice

# Function to get user symptoms and their severity
def get_symptoms():
    print("\nHere are some common symptoms:")
    for i, symptom in enumerate(common_symptoms, 1):
        print(f"{i}. {symptom}")
    print("\nEnter the numbers of your symptoms (separated by commas):")
    user_input = input("Example: 1, 2, 3\n").strip()
    selected_indices = [int(index.strip()) - 1 for index in user_input.split(",")]
    symptoms = []
    for index in selected_indices:
        symptom = common_symptoms[index]
        severity = input(f"How severe is your '{symptom}'? (1 = Mild, 2 = Moderate, 3 = Severe): ").strip()
        symptoms.append((symptom, int(severity)))
    return symptoms

# Function to diagnose based on symptoms and severity
def diagnose(symptoms):
    disease_scores = {}
    for disease, details in diseases.items():
        disease_symptoms = details["symptoms"]
        score = 0
        for symptom, severity in symptoms:
            if symptom in disease_symptoms:
                score += severity  # Add severity to the score
        if score > 0:
            disease_scores[disease] = {
                "score": score,
                "severity": details["severity"]
            }
    # Sort diseases by score (highest first)
    sorted_diseases = sorted(disease_scores.items(), key=lambda x: x[1]["score"], reverse=True)
    return sorted_diseases

# Function to display diagnosis results
def display_results(sorted_diseases):
    if sorted_diseases:
        print("\n=== Diagnosis Results ===")
        for disease, details in sorted_diseases:
            print(f"\nPossible Disease: {disease}")
            print(f"Severity: {details['severity']}")
            print(f"Confidence Score: {details['score']}")
            if details["severity"] == "Mild":
                print("Recommendation: Rest at home and drink plenty of fluids.")
            elif details["severity"] == "Moderate":
                print("Recommendation: Consult a doctor and take prescribed medication.")
            elif details["severity"] == "High":
                print("Recommendation: Seek immediate medical attention.")
        print("\nTake care and get well soon!")
    else:
        print("\nNo matching diseases found. Please consult a doctor for further evaluation.")

# Function to display symptom history
def display_history():
    if not symptom_history:
        print("\nNo history found. Please check your symptoms first.")
    else:
        print("\n=== Symptom History ===")
        for i, entry in enumerate(symptom_history, 1):
            print(f"\nEntry {i}:")
            print(f"Symptoms: {', '.join([s[0] for s in entry['symptoms']])}")
            print(f"Diagnosis: {entry['diagnosis']}")
            print(f"Date: {entry['date']}")

# Function to display health tips
def display_health_tips():
    print("\n=== Health Tips ===")
    print("1. Drink plenty of water to stay hydrated.")
    print("2. Get at least 7-8 hours of sleep every night.")
    print("3. Eat a balanced diet rich in fruits and vegetables.")
    print("4. Exercise regularly to boost your immune system.")
    print("5. Wash your hands frequently to prevent infections.")
    print("6. Avoid stress by practicing mindfulness or meditation.")

# Main program
def main():
    from datetime import datetime
    while True:
        choice = display_menu()
        if choice == "1":
            # Get user symptoms
            user_symptoms = get_symptoms()
            print(f"\nYou entered the following symptoms: {', '.join([s[0] for s in user_symptoms])}")

            # Diagnose based on symptoms
            sorted_diseases = diagnose(user_symptoms)

            # Display results
            display_results(sorted_diseases)

            # Save to history
            if sorted_diseases:
                diagnosis = [disease for disease, _ in sorted_diseases]
                symptom_history.append({
                    "symptoms": user_symptoms,
                    "diagnosis": diagnosis,
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
        elif choice == "2":
            # Display symptom history
            display_history()
        elif choice == "3":
            # Display health tips
            display_health_tips()
        elif choice == "4":
            print("\nThank you for using the Medical Diagnosis System. Stay healthy!")
            break
        else:
            print("\nInvalid choice. Please try again.")

        # Ask if the user wants to continue
        restart = input("\nDo you want to continue? (yes/no): ").strip().lower()
        if restart != "yes":
            print("\nThank you for using the Medical Diagnosis System. Stay healthy!")
            break

# Run the program
if __name__ == "__main__":
    main()