import sys

brioche_number = int(input())

max_score = -sys.maxsize

best_baker = False

for brioche in range(brioche_number):
    baker_name = input()
    total_score = 0
    while True:
        command = input()
        if command == "Stop":
            print(f"{baker_name} has {total_score} points.")
            if best_baker:
                print(f"{number_1} is the new number 1!")
                best_baker = False
            break
        brioche_score = int(command)
        total_score += brioche_score
        if total_score > max_score:
            max_score = total_score
            number_1 = baker_name
            best_baker = True

print(f"{number_1} won competition with {max_score} points!")