WRAPPING_PAPER = 5.80
FABRIC = 7.20
GLUE = 1.20

number_wrapping_paper = int(input())
number_fabric = int(input())
number_glue = float(input())
discount_percentage = int(input())

wrapping_paper_price = number_wrapping_paper * WRAPPING_PAPER
fabric_price = number_fabric * FABRIC
glue_price = number_glue * GLUE
total_price = wrapping_paper_price + fabric_price + glue_price
final_price = total_price - (total_price * discount_percentage / 100)

print(f"{final_price:.3f}")