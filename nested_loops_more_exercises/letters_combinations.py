start = input()
finish = input()
pass_letter = input()

combinations = 0

for letter_1 in range(ord(start), ord(finish) + 1):
    for letter_2 in range(ord(start), ord(finish) + 1):
        for letter_3 in range(ord(start), ord(finish) + 1):

          if pass_letter not in chr(letter_1) + chr(letter_2) + chr(letter_3):
              combinations += 1
              print(chr(letter_1) + chr(letter_2) + chr(letter_3), end = " ")

print(combinations)
