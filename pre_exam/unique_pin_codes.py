first_limit = int(input())
second_limit = int(input())
third_limit = int(input())

for num1 in range(1, first_limit + 1):
    if num1 % 2 == 0:
        for num2 in range(1, second_limit + 1):
            if num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7:
                for num3 in range(1, third_limit + 1):
                    if num3 % 2 == 0:
                        print(num1, num2, num3)
