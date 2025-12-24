a = int(input())
b = int(input())
cap = int(input())

count = 0
A = 35
B = 64

for x in range(1, a + 1):
    for y in range(1, b + 1):
        if count >= cap:
            break

        password = chr(A) + chr(B) + str(x) + str(y) + chr(B) + chr(A)
        print(password, end="|")
        count += 1

        B += 1
        if B > 96:
            B = 64
        A += 1
        if A > 55:
            A = 35

    if count >= cap:
        break