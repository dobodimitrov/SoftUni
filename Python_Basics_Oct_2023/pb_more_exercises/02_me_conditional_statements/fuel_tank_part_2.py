GASOLINE = 2.22
DIESEL = 2.33         # per liter
GAS = 0.93

GASOLINE_DISCOUNT = GASOLINE - 0.18
DIESEL_DISCOUNT = DIESEL - 0.12
GAS_DISCOUNT = GAS - 0.08

type_fuel = input()
litres_fuel = float(input())
discount_card = input()

total_gas_price = 0

if type_fuel == "Gasoline":
    if discount_card == "Yes":
        total_gas_price += GASOLINE_DISCOUNT * litres_fuel
    if discount_card == "No":
        total_gas_price += GASOLINE * litres_fuel
elif type_fuel == "Diesel":
    if discount_card == "Yes":
        total_gas_price += DIESEL_DISCOUNT * litres_fuel
    if discount_card == "No":
        total_gas_price += DIESEL * litres_fuel
elif type_fuel == "Gas":
    if discount_card == "Yes":
        total_gas_price += GAS_DISCOUNT * litres_fuel
    if discount_card == "No":
        total_gas_price += GAS * litres_fuel
if 20 <= litres_fuel <= 25:
    total_gas_price *= 0.92
elif litres_fuel > 25:
    total_gas_price *= 0.9

print(f"{total_gas_price:.2f} lv.")




    # if 20 <= litres_fuel <= 25:
    #     total_gas_price *= 0.92
    # elif litres_fuel > 25:
    #     total_gas_price *= 0.9