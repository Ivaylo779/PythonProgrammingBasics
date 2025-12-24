wins = 0
losses = 0
total_matches = 0

while True:
    tournament_name = input()
    if tournament_name == "End of tournaments":
        print(f"{(wins / total_matches) * 100:.2f}% matches win")
        print(f"{(losses / total_matches) * 100:.2f}% matches lost")
        break
    matches = int(input())
    total_matches += matches
    for match in range(1, matches + 1):
        desi_points = int(input())
        opponent_points = int(input())
        if desi_points > opponent_points:
            wins += 1
            print(f"Game {match} of tournament {tournament_name}: win with {desi_points - opponent_points} points.")
        else:
            losses += 1
            print(f"Game {match} of tournament {tournament_name}: lost with {opponent_points - desi_points} points.")