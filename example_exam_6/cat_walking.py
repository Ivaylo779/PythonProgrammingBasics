daily_stroll = int(input())
strolls_per_day = int(input())
daily_calorie_intake = int(input())

total_minutes = daily_stroll * strolls_per_day
burned_calories = total_minutes * 5

if burned_calories >= daily_calorie_intake * 0.50:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")



