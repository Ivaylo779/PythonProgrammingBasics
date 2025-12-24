annual_tax = int(input())

basketball_shoes = annual_tax - (annual_tax * 0.40)
basketball_kit = basketball_shoes - (basketball_shoes * 0.20)
basketball = basketball_kit * 0.25
basketball_trinkets = basketball * 0.20

final_price = annual_tax + basketball_shoes + basketball_kit + basketball + basketball_trinkets

print(final_price)

