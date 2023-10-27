volume = int(input())
debit_1 = int(input())
debit_2 = int(input())
hours_gone = float(input())

litres_debit_1 = debit_1 * hours_gone
litres_debit_2 = debit_2 * hours_gone
total_litres_in = litres_debit_1 + litres_debit_2
percentage_full = (total_litres_in / volume) * 100
percentage_debit_1 = (litres_debit_1 / total_litres_in) * 100
percentage_debit_2 = (litres_debit_2 / total_litres_in) * 100
litres_over = total_litres_in - volume

if total_litres_in <= volume:
    print(f"The pool is {percentage_full:.2f}% full. Pipe 1: {percentage_debit_1:.2f}%. "
          f"Pipe 2: {percentage_debit_2:.2f}%.")
else:
    print(f"For {hours_gone:.2f} hours the pool overflows with {litres_over:.2f} liters.")
