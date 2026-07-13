diseases = {
    "Flu": ["fever", "cough", "body pain"],
    "Viral Infection": ["fever", "headache", "fatigue"],
    "Diabetes": ["frequent urination", "excessive thirst", "weight loss"],
    "Heart Disease": ["chest pain", "shortness of breath", "fatigue"],
    "Migraine": ["headache", "nausea", "sensitivity to light"]
}

print("\n===== AI MEDICAL DIAGNOSIS SYSTEM =====")
print("\nAvailable Symptoms:")

all_symptoms = set()
for symptom_list in diseases.values():
    for symptom in symptom_list:
        all_symptoms.add(symptom)

for symptom in sorted(all_symptoms):
    print("-", symptom)

print("\nEnter symptoms separated by commas")
user_input = input("Symptoms: ").lower()
user_symptoms = [s.strip() for s in user_input.split(",")]

best_disease = None
best_score = 0

for disease, symptoms in diseases.items():
    score = 0
    for symptom in symptoms:
        if symptom in user_symptoms:
            score += 1
            
    if score > best_score:
        best_score = score
        best_disease = disease

print("\n===== DIAGNOSIS RESULT =====")
if best_score > 0:
    print("Possible Disease:", best_disease)
    print("Matched Symptoms:", best_score)
else:
    print("No matching disease found.")

print("Channaveerayya Gandhadha.\n 2403031460094")