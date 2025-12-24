from math import floor

tournament_number = int(input())
points = int(input())
points_gained = 0
wins = 0

for _ in range(tournament_number):
    tournament_stage = input()
    if tournament_stage == "W":
        points_gained += 2000
        wins += 1
    elif tournament_stage == "F":
        points_gained += 1200
    elif tournament_stage == "SF":
        points_gained += 720

points += points_gained
average_points = points_gained / tournament_number
win_percentage = (wins / tournament_number) * 100

print(f"Final points: {points}")
print(f"Average points: {floor(average_points)}")
print(f"{win_percentage:.2f}%")