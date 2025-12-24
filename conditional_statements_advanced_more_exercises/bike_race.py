junior_cyclists = int(input())
senior_cyclists = int(input())
track = input()
junior_price = 0
senior_price = 0

if track == "trail":
    junior_price = 5.50
    senior_price = 7
elif track == "cross-country":
    junior_price = 8
    senior_price = 9.50
    if junior_cyclists + senior_cyclists >= 50:
        junior_price *=  0.75
        senior_price *= 0.75
elif track == "downhill":
    junior_price = 12.25
    senior_price = 13.75
elif track == "road":
    junior_price = 20
    senior_price = 21.50

total_sum = junior_price * junior_cyclists + senior_price * senior_cyclists
donated_money = total_sum * 0.95

print(f"{donated_money:.2f}")

