square_meters = float(input())
price_for_one_square_meter = 7.61
price_for_yard_greening = square_meters * price_for_one_square_meter
discount = price_for_yard_greening * 0.18
final_price = price_for_yard_greening - discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")