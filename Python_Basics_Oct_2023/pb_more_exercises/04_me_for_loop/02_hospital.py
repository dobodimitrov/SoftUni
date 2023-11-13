days = int(input())
doctors = 7
untreated_patients = 0
treated_patients = 0

for period in range(1, days+1):
    patients_today = int(input())
    if period % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    if patients_today > doctors:
        untreated_patients += patients_today - doctors
        treated_patients += doctors
    else:
        treated_patients += patients_today

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
