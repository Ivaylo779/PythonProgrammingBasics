fitness_visitors = int(input())
back = 0
chest = 0
legs = 0
abs= 0
protein_shakes = 0
protein_bar = 0
training = 0
protein = 0

for _ in range(fitness_visitors):
    activity = input()
    if activity == "Back":
        back += 1
        training += 1
    elif activity == "Chest":
        chest += 1
        training += 1
    elif activity == "Legs":
        legs += 1
        training += 1
    elif activity == "Abs":
        abs += 1
        training += 1
    elif activity == "Protein shake":
        protein_shakes += 1
        protein += 1
    elif activity == "Protein bar":
        protein_bar += 1
        protein += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shakes} - protein shake")
print(f"{protein_bar} - protein bar")
training_percentage = training / fitness_visitors * 100
protein_percentage = protein / fitness_visitors * 100
print(f"{training_percentage:.2f}% - work out")
print(f"{protein_percentage:.2f}% - protein")