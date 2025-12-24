film_name = input()
hall_type = input()
ticket_number = int(input())
price = 0

if hall_type == "normal":
    if film_name == "A Star Is Born":
        price = 7.50
    elif film_name == "Bohemian Rhapsody":
        price = 7.35
    elif film_name == "Green Book":
        price = 8.15
    elif film_name == "The Favourite":
        price = 8.75
elif hall_type == "luxury":
    if film_name == "A Star Is Born":
        price = 10.50
    elif film_name == "Bohemian Rhapsody":
        price = 9.45
    elif film_name == "Green Book":
        price = 10.25
    elif film_name == "The Favourite":
        price = 11.55
elif hall_type == "ultra luxury":
    if film_name == "A Star Is Born":
        price = 13.50
    elif film_name == "Bohemian Rhapsody":
        price = 12.75
    elif film_name == "Green Book":
        price = 13.25
    elif film_name == "The Favourite":
        price = 13.95

income = ticket_number * price

print(f"{film_name} -> {income:.2f} lv.")