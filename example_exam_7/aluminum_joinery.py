window_frames = int(input())
window_frame_type = input()
delivery_method = input()

if window_frame_type  == "90X130":
    price = 110
    if window_frames > 60:
        price *= 0.92
    elif window_frames > 30:
        price *= 0.95
elif window_frame_type == "100X150":
    price = 140
    if window_frames > 80:
        price *= 0.90
    elif window_frames > 40:
        price *= 0.94
elif window_frame_type == "130X180":
    price = 190
    if window_frames > 50:
        price *= 0.88
    elif window_frames > 20:
        price *= 0.93
elif window_frame_type == "200X300":
    price = 250
    if window_frames > 50:
        price *= 0.86
    elif window_frames > 25:
        price *= 0.91

total_price = window_frames * price

if delivery_method == "With delivery":
    total_price += 60

if window_frames > 99:
    total_price *= 0.96

if window_frames > 10:
    print(f"{total_price:.2f} BGN")
else:
    print("Invalid order")