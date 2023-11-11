desired_height = int(input())
has_succeeded = True
current_height = desired_height - 30
fails = 0
total_jumps = 0

while current_height < desired_height + 1:
    current_jump = int(input())
    total_jumps += 1
    if current_jump <= current_height:
        fails += 1
        if fails == 3:
            has_succeeded = False
            break
        continue
    else:
        fails = 0
        current_height += 5

if has_succeeded:
    print(f"Tihomir succeeded, he jumped over {desired_height}cm after {total_jumps} jumps.")
if not has_succeeded:
    print(f"Tihomir failed at {current_height}cm after {total_jumps} jumps.")
