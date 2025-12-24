minutes_control = int(input())
seconds_control = int(input())
chute_length = float(input())
seconds_for_100_meters = int(input())

total_seconds_control = minutes_control * 60 + seconds_control
time_decrease = chute_length / 120
total_time_decrease = time_decrease * 2.5

marin_time = (chute_length / 100) * seconds_for_100_meters - total_time_decrease

if marin_time <= total_seconds_control:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {marin_time:.3f}.")
else:
    diff = total_seconds_control - marin_time
    print(f"No, Marin failed! He was {abs(diff):.3f} second slower.")