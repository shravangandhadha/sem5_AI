doctors = ["Dr. Smith", "Dr. Johnson", "Dr. Lee"]
slots = ["Morning", "Afternoon", "Evening"]
schedule = {}
def assign_doctor(index):
    if index == len(doctors):
        return True
    doctor = doctors[index]
    for slot in slots:
        if slot not in schedule.values():
            schedule[doctor] = slot
            if assign_doctor(index + 1):
                return True
            del schedule[doctor]
    return False
assign_doctor(0)
print("--------- HOSPITAL SCHEDULE ---------")
for doctor in doctors:
    slot = schedule.get(doctor)
    if slot:
        print(f"{doctor} -> {slot} slot.")
    else:
        print(f"{doctor} has no assigned slot.")
print("Channaveerayya, 2403031460094")
    