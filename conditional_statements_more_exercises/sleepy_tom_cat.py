days_off = int(input())

work_days = 365 - days_off
work_play_time = work_days * 63
free_play_time = days_off * 127
total_play_time = work_play_time + free_play_time

if total_play_time > 30000:
    diff = total_play_time - 30000
    hours = diff // 60
    minutes = diff % 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    diff = 30000 - total_play_time
    hours = diff // 60
    minutes = diff % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")