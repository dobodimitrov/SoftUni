number_of_students = int(input())
total_grade = 0
fail_count = 0
count_3_to_4 = 0
count_4_to_5 = 0
top_count = 0
for grades in range(0, number_of_students):
    current_grade = float(input())
    total_grade += current_grade
    if current_grade < 3.00:
        fail_count += 1
    elif 3.00 <= current_grade < 4.00:
        count_3_to_4 += 1
    elif 4.00 <= current_grade < 5.00:
        count_4_to_5 += 1
    else:
        top_count += 1

avg_grade = total_grade / number_of_students
fail_percentage = fail_count / number_of_students * 100
percentage_3_to_4 = count_3_to_4 / number_of_students * 100
percentage_4_to_5 = count_4_to_5 / number_of_students * 100
percentage_top = top_count / number_of_students * 100

print(f"Top students: {percentage_top:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_4_to_5:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_3_to_4:.2f}%")
print(f"Fail: {fail_percentage:.2f}%")
print(f"Average: {avg_grade:.2f}")
