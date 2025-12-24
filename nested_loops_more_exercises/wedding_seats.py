last_sector = input()
rows_in_first_sector = int(input())
seats_on_odd_row = int(input())

total_seats = 0

for sector_code in range(ord('A'), ord(last_sector) + 1):
    sector_letter = chr(sector_code)
    sector_index = sector_code - ord('A')
    rows_in_current_sector = rows_in_first_sector + sector_index

    for row in range(1, rows_in_current_sector + 1):
        if row % 2 != 0:
            seats = seats_on_odd_row
        else:
            seats = seats_on_odd_row + 2

        for seat_code in range(ord('a'), ord('a') + seats):
            seat_letter = chr(seat_code)
            print(sector_letter + str(row) + seat_letter)
            total_seats += 1

print(total_seats)