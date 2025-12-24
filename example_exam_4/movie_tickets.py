a1 = int(input())
a2 = int(input())
n = int(input())

for ascii_code in range(a1, a2):
    symbol_1 = chr(ascii_code)
    for symbol_2 in range(1, n):
        for symbol_3 in range(1,  (n // 2)):
            symbol_4 = ascii_code
            if ascii_code % 2 != 0 and (symbol_2 + symbol_3 + symbol_4) % 2 != 0:
                print(f"{str(symbol_1)}-{str(symbol_2)}{str(symbol_3)}{str(symbol_4)}")

