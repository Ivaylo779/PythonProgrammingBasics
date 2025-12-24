airline_name = input()
adult_tickets = int(input())
children_tickets = int(input())
adult_ticket_net_price = float(input())
service_fee = float(input())

children_ticket_net_price = adult_ticket_net_price * 0.30

child_tickets_price = children_ticket_net_price + service_fee
adult_tickets_price = adult_ticket_net_price + service_fee

total_price = children_tickets * child_tickets_price + adult_tickets * adult_tickets_price

final_profit = total_price * 0.20

print(f"The profit of your agency from {airline_name} tickets is {final_profit:.2f} lv.")