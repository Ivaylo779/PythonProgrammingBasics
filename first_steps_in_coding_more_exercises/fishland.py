mackerel_price = float(input())
sprat_price = float(input())
bonito_kg = float(input())
safrid_kg = float(input())
mussels_kg = int(input())

bonito_price_kg = mackerel_price + (mackerel_price * 0.60)
safrid_price_kg = sprat_price + (sprat_price * 0.80)

bonito_price = bonito_kg * bonito_price_kg
safrid_price = safrid_kg * safrid_price_kg
mussels_price = mussels_kg * 7.50

sum = bonito_price + safrid_price + mussels_price

print(f"{sum: .2f}")
