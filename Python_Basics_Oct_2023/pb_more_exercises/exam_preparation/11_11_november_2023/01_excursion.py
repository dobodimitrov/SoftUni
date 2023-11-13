NIGHT = 20.00
TRANSPORT_CARD = 1.60
MUSEUM_TICKET = 6.00

people_count = int(input())
nights_count = int(input())
transport_card_count = int(input())
museum_ticket_count = int(input())

cost_per_person = nights_count * NIGHT + transport_card_count * TRANSPORT_CARD + museum_ticket_count * MUSEUM_TICKET
total_cost = 1.25 * (people_count * cost_per_person)         # additional expenses | 25% of total cost |

print(f"{total_cost:.2f}")