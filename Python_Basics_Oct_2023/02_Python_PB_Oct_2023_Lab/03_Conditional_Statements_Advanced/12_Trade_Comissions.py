city = input()
sales_volume = float(input())
commission = 0

if city == "Sofia":
    if 0 <= sales_volume <= 500:
        commission = 0.05
    elif 500 < sales_volume <= 1000:
        commission = 0.07
    elif 1000 < sales_volume <= 10000:
        commission = 0.08
    elif sales_volume > 10000:
        commission = 0.12
    else:
        print("error")
elif city == "Varna":
    if 0 <= sales_volume <= 500:
        commission = 0.045
    elif 500 < sales_volume <= 1000:
        commission = 0.075
    elif 1000 < sales_volume <= 10000:
        commission = 0.10
    elif sales_volume > 10000:
        commission = 0.13
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= sales_volume <= 500:
        commission = 0.055
    elif 500 < sales_volume <= 1000:
        commission = 0.08
    elif 1000 < sales_volume <= 10000:
        commission = 0.12
    elif sales_volume > 10000:
        commission = 0.145
    else:
        print("error")
else:
    print("error")

commission_amount = commission * sales_volume
if sales_volume >= 0 and (city == "Sofia" or city == "Plovdiv" or city == "Varna"):
    print(f'{commission_amount:.2f}')
