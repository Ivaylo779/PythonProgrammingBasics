trunk_capacity = float(input())

suitcases = 0
baggage = 0
count = 0

while True:
    command = input()
    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    count += 1
    suitcase_size = float(command)
    if count % 3 == 0:
        suitcase_size += suitcase_size * 0.10
    if suitcase_size + baggage > trunk_capacity:
        print("No more space!")
        break
    baggage += suitcase_size
    suitcases += 1

print(f"Statistic: {suitcases} suitcases loaded.")