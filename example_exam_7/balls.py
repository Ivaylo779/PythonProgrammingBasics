from math import floor

balls = int(input())

points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
total_divisions = 0
diff_balls = 0

for _ in range(balls):
    color = input()
    if color == "red":
        points += 5
        red_balls += 1
    elif color == "orange":
        points += 10
        orange_balls += 1
    elif color == "yellow":
        points += 15
        yellow_balls += 1
    elif color == "white":
        points += 20
        white_balls += 1
    elif color == "black":
        points = floor(points / 2)
        black_balls += 1
        total_divisions += 1
    else:
        diff_balls += 1

print(
    f"Total points: {points}\n"
    f"Red balls: {red_balls}\n"
    f"Orange balls: {orange_balls}\n"
    f"Yellow balls: {yellow_balls}\n"
    f"White balls: {white_balls}\n"
    f"Other colors picked: {diff_balls}\n"
    f"Divides from black balls: {total_divisions}\n"
)