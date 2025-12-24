days = int(input())
room_type = input()
grade = input()

room_for_one_person = 18.00
apartment = 25.00
president_apartment = 35.00
discount = 0

nights = days - 1

if room_type == "room for one person":
    total_sum = room_for_one_person * nights
    discount = total_sum
elif room_type == "apartment":
    total_sum = apartment * nights
    if days < 10:
        discount = total_sum - (total_sum * 0.30)
    elif 10 <= days <= 15:
        discount = total_sum - (total_sum * 0.35)
    else:
        discount = total_sum - (total_sum * 0.50)
elif room_type == "president apartment":
    total_sum = president_apartment * nights
    if days < 10:
        discount = total_sum - (total_sum * 0.10)
    elif 10 <= days <= 15:
        discount = total_sum - ( total_sum * 0.15)
    else:
        discount =total_sum - (total_sum * 0.20)

if grade == "positive":
    total_sum = discount + (discount * 0.25)
else:
    total_sum = discount - (discount * 0.10)

print(f"{total_sum:.2f}")



