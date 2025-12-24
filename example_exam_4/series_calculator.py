from math import floor

series_name = input()
seasons = int(input())
episodes = int(input())
duration = float(input())

add_duration = duration * 0.20
episode_duration = duration + add_duration
special_episodes = seasons * 10

total_time = episode_duration * episodes * seasons + special_episodes

print(f"Total time needed to watch the {series_name} series is {floor(total_time)} minutes.")

