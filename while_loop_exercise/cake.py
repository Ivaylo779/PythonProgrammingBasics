cake_length = int(input())
cake_width = int(input())
pieces = ""
cake_number = cake_length * cake_width

while True:
    pieces = input()
    if pieces == "STOP":
        break
    piece_count = int(pieces)
    cake_number -= piece_count
    if cake_number <= 0:
        break

if pieces == "STOP":
    print(f"{cake_number} pieces are left.")

if cake_number <= 0:
    print(f"No more cake left! You need {(abs(cake_number))} pieces more.")