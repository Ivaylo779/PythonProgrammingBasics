from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
climbing_1_meter_time = float(input()) 

total_time = distance_in_meters * climbing_1_meter_time
total_time += floor(distance_in_meters / 50) * 30

if total_time < record_in_seconds:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    missing_seconds = record_in_seconds - total_time
    print(f"No! He was {abs(missing_seconds):.2f} seconds slower.")