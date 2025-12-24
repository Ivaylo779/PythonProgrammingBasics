filming_time = int(input())
scenes = int(input())
scene_duration = int(input())

preparation = filming_time * 0.15
total_duration = (scene_duration * scenes) + preparation

if total_duration <= filming_time:
    diff = filming_time - total_duration
    print(f"You managed to finish the movie on time! You have {round(diff)} minutes left!")
else:
    diff = total_duration - filming_time
    print(f"Time is up! To complete the movie you need {diff:.0f} minutes.")