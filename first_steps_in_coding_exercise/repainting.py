NAYLON = 1.50
PAINT = 14.50
PAINT_THINNER = 5.00

required_naylon = int(input())
required_paint = int(input())
required_thinner = int(input())
hours_of_work = int(input())

full_nylon_req = (required_naylon + 2) * NAYLON
full_paint_req = (required_paint + (required_paint * 0.10))* PAINT
full_thinner_req = required_thinner * PAINT_THINNER

total_sum = full_nylon_req + full_paint_req + full_thinner_req + 0.40
painter_check = (total_sum * 0.30) * hours_of_work
final_price = painter_check + total_sum

print(final_price)