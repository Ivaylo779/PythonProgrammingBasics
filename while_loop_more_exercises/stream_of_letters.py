c = True
o = True
n = True
word = ""
full_word = ""

while True:
    symbol = input()

    if symbol == "End":
        break

    if not (('a' <= symbol <= 'z') or ('A' <= symbol <= 'Z')):
        continue

    if symbol == "c":
        if c:
            c = False
        else:
            word += symbol
    elif symbol == "o":
        if o:
            o = False
        else:
            word += symbol
    elif symbol == "n":
        if n:
            n = False
        else:
            word += symbol
    else:
        word += symbol

    if not c and not o and not n:
        full_word += word + " "
        c = True
        o = True
        n = True
        word = ""

print(full_word)