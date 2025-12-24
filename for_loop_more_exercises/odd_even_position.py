import sys

n = int(input())
odd_sum = 0
even_sum = 0

min_even_number = sys.maxsize
max_even_number = -sys.maxsize
min_odd_number = sys.maxsize
max_odd_number = -sys.maxsize

odd_exists = False
even_exists = False

for num in range(1, n + 1):
    new_number = float(input())
    if num % 2 == 0:
        even_sum += new_number
        even_exists = True
        if new_number < min_even_number:
            min_even_number = new_number
        if new_number > max_even_number:
            max_even_number = new_number
    else:
        odd_sum += new_number
        odd_exists = True
        if new_number < min_odd_number:
            min_odd_number = new_number
        if new_number > max_odd_number:
            max_odd_number = new_number

print(f"OddSum={odd_sum:.2f},")
if odd_exists:
    print (f"OddMin={min_odd_number:.2f},")
    print(f"OddMax={max_odd_number:.2f},")
else:
    print(f"OddMin=No,")
    print(f"OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
if even_exists:
    print(f"EvenMin={min_even_number:.2f},")
    print(f"EvenMax={max_even_number:.2f}")
else:
    print(f"EvenMin=No,")
    print(f"EvenMax=No")