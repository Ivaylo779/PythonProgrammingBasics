locations = int(input())

for _ in range(locations):
    average_yield = float(input())
    days_working = int(input())
    total_gold = 0

    for _ in range(days_working):
        new_input = float(input())
        total_gold += new_input

    average_gold = total_gold / days_working

    if average_gold >= average_yield:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
    else:
        diff = average_yield - average_gold
        print(f"You need {diff:.2f} gold.")
