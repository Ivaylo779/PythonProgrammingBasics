from math import ceil, floor

paint_boxes = int(input())
wallpaper_rolls = int(input())
gloves_price = float(input())
brush_price = float(input())

paint_box_price = 21.50 * paint_boxes
wallpaper_roll_price = 5.20 * wallpaper_rolls
glove_number = ceil(wallpaper_rolls * 0.35)
brush_number = floor(paint_boxes * 0.48)
total_glove_price = glove_number * gloves_price
total_brush_price = brush_number * brush_price
all_product_price = total_glove_price + total_brush_price + paint_box_price + wallpaper_roll_price
final_price = all_product_price / 15

print(f"This delivery will cost {final_price:.2f} lv." )

