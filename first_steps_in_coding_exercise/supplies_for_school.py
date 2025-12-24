PEN_PACKAGE = 5.80
MARKER_PACKAGE = 7.20
BOARD_CLEANER = 1.20

number_of_pen_packages = int(input())
number_of_marker_packages = int(input())
liters_of_board_cleaner = int(input())
discount_percentage = int(input())

pen_packages_price = number_of_pen_packages * PEN_PACKAGE
marker_packages_price = number_of_marker_packages * MARKER_PACKAGE
board_cleaner_price = liters_of_board_cleaner * BOARD_CLEANER

total_price = pen_packages_price + marker_packages_price + board_cleaner_price
final_price = total_price - (total_price * discount_percentage / 100)

print(final_price)

