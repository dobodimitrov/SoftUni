student = input()
times_failed = 0
total_grade = 0
current_class = 1
is_excluded = False

while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        times_failed += 1
        if times_failed > 1:
            is_excluded = True
            break
        continue
    else:
        current_class += 1
        total_grade += current_grade

if is_excluded:
    print(f"{student} has been excluded at {int(current_class)} grade")
else:
    average_grade = total_grade / 12
    print(f"{student} graduated. Average grade: {average_grade:.2f}")
