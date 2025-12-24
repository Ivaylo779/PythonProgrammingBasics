savings = 0
destination = ""

while True:
    destination = input()
    if destination == "End":
        break
    minimal_budget = float(input())
    while True:
        sum = float(input())
        savings += sum
        if savings >= minimal_budget:
            print(f"Going to {destination}!")
            savings = 0
            break

