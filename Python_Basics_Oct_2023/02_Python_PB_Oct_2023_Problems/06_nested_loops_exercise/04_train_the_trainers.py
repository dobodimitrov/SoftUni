number_of_judges = int(input())
name = input()
total_marks = 0
presentations_total = 0
presentations_counter = 0

while name != "Finish":
    presentations_counter += 1

    for marks in range(1, number_of_judges + 1):
        mark = float(input())
        total_marks += mark

    presentation_mark = total_marks / number_of_judges
    presentations_total += presentation_mark
    print(f"{name} - {presentation_mark:.2f}.")
    total_marks = 0
    name = input()

avg_score = presentations_total / presentations_counter
print(f"Student's final assessment is {avg_score:.2f}.")
