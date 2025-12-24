sold_games = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for _ in range(sold_games):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone += 1
    elif game_name == "Fornite":
        fornite += 1
    elif game_name == "Overwatch":
        overwatch += 1
    else:
        others += 1

hearthstone_percentage = (hearthstone / sold_games) * 100
print(f"Hearthstone - {hearthstone_percentage:.2f}%")
fortnite_percentage = (fornite / sold_games) * 100
print(f"Fornite - {fortnite_percentage:.2f}%")
overwatch_percentage = (overwatch / sold_games) * 100
print(f"Overwatch - {overwatch_percentage:.2f}%")
others_percentage = (others / sold_games) * 100
print(f"Others - {others_percentage:.2f}%")

