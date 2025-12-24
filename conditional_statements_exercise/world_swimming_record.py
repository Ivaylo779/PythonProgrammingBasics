record_in_seconds = float(input())
distance_in_meters = float(input())
time_swimming = float(input())

swimming = distance_in_meters * time_swimming
resistance = (distance_in_meters // 15) * 12.5
total_time = swimming + resistance

if total_time < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    total_time -= record_in_seconds
    print(f"No, he failed! He was {total_time:.2f} seconds slower.")


