month = input()
hours_spent = int(input())
people_in_group = int(input())
time_of_day = input()
price = 0

if month == "march" or month == "april" or month == "may":
    if time_of_day == "day":
        price += 10.50
    else:
        price += 8.40
elif month == "june" or month == "july" or month == "august":
    if time_of_day == "day":
        price += 12.60
    else:
        price += 10.20

if people_in_group >= 4:
    price = price - (price * 0.10)

if hours_spent >= 5:
    price = price - (price * 0.50)

total_sum = (price * people_in_group) * hours_spent

print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {total_sum:.2f}")