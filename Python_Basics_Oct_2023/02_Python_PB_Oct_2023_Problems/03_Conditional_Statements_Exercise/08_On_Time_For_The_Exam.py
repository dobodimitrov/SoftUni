
start_hour = int(input())
start_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

start_time_as_min = start_hour * 60 + start_minutes
arrival_time_as_min = arrival_hour * 60 + arrival_minutes
diff = start_time_as_min - arrival_time_as_min

mm = 0
hh = 0
if arrival_time_as_min > start_time_as_min:
    print("Late")
    hh = abs(diff) // 60
    mm = abs(diff) % 60
    if 0 < diff < 60:
        print(f'{abs(diff)} minutes after the start')
    if hh != 0:
        print(f'{abs(hh)}:{abs(mm):02d} hours after the start')
    else:
        print(f'{mm} minutes after the start')
elif 0 <= diff <= 30:
    print("On time")
    if diff != 0:
        print(f'{diff} minutes before the start')
elif diff > 30:
    print("Early")
    hh = diff // 60
    mm = diff % 60
    if diff < 60:
        print(f'{mm} minutes before the start')
    else:
        print(f'{hh}:{mm:02d} hours before the start')


# · "Late", ако студентът пристига по-късно от часа на изпита;
# · "On time", ако студентът пристига точно в часа на изпита или до 30 минути по-рано;
# · "Early", ако студентът пристига повече от 30 минути преди часа на изпита.

# · "mm minutes before the start" за идване по-рано с по-малко от час;
# · "hh:mm hours before the start" за подраняване с 1 час или повече.
# Минутите винаги печатайте с 2 цифри, например "1:05”;
# · "mm minutes after the start" за закъснение под час;
# · "hh:mm hours after the start" за закъснение от 1 час или повече.
# Минутите винаги печатайте с 2 цифри, например "1:03”.
