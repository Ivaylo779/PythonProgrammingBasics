group_number = int(input())
total_people = 0
musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for _ in range(group_number):
    people_in_group = int(input())
    total_people += people_in_group
    if people_in_group <= 5:
        musala += people_in_group
    elif 6 <= people_in_group <= 12:
        montblanc += people_in_group
    elif 13 <= people_in_group <= 25:
        kilimanjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        k2 += people_in_group
    elif people_in_group >= 41:
        everest += people_in_group

print(f"{(musala / total_people) * 100:.2f}%")
print(f"{(montblanc / total_people) * 100:.2f}%")
print(f"{(kilimanjaro / total_people) * 100:.2f}%")
print(f"{(k2 / total_people) * 100:.2f}%")
print(f"{(everest / total_people) * 100:.2f}%")