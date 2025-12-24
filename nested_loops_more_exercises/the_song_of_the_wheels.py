control_value = int(input())

count = 0

for a in range(1,10):
    for b in range(1,10):
        if a >= b:
            continue
        for c in range(1,10):
            for d in range(1,10):
                if c <= d:
                    continue
                if a * b + c * d == control_value:
                    count += 1
                    if count == 4:
                        password = str(a) + str(b) + str(c) + str(d)
                    print(str(a) + str(b) + str(c) + str(d), end = " ")

print()

if count >= 4:
    print(f"Password: {password}")
else:
    print("No!")

