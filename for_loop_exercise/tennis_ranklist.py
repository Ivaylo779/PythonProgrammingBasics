from math import floor
tournament_count = int(input())
starter_points = int(input())
win_count = 0
points = 0

for _ in range(tournament_count):
    tournament_stage = input()
    if tournament_stage == "W":
        points += 2000
        win_count += 1
    elif tournament_stage == "F":
        points += 1200
    elif tournament_stage == "SF":
        points += 720

total_points = points + starter_points
average_points = points / tournament_count
win_percentage = (win_count / tournament_count) * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{win_percentage:.2f}%")