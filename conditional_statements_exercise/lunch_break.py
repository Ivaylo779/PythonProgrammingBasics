from math import ceil

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
relax_time = break_duration / 4
free_time = break_duration - lunch_time - relax_time

if free_time >= episode_duration:
    bonus_time = free_time - episode_duration

    print(f"You have enough time to watch {series_name} and left with {ceil(bonus_time)} minutes free time.")
else:
    not_enough = episode_duration - free_time

    print(f"You don't have enough time to watch {series_name}, you need {ceil(not_enough)} more minutes.")

