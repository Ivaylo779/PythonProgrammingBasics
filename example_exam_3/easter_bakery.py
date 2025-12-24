flour_price = float(input())
flour_kgs = float(input())
sugar_kgs = float(input())
egg_cartons = int(input())
yeast_packets = int(input())

sugar_price = flour_price - (flour_price * 0.25)
egg_carton_price = flour_price + (flour_price * 0.10)
yeast_packet_price = sugar_price - (sugar_price * 0.80)

total_price = (flour_price * flour_kgs + sugar_price * sugar_kgs +
               egg_carton_price * egg_cartons + yeast_packet_price * yeast_packets)

print(f"{total_price:.2f}")