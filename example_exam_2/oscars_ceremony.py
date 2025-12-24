hall_rent = int(input())

statuettes = hall_rent - (hall_rent * 0.30)
catering = statuettes - (statuettes * 0.15)
sound_recording = catering * 1/2

total_sum = hall_rent + statuettes + catering + sound_recording

print(f"{total_sum:.2f}")