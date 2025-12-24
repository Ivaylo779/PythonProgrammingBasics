from math import floor

ascii_sum = 0
max_word_power = 0

while True:
    word = input()
    if word == "End of words":
        break
    ascii_sum = 0
    for char in word:
        ascii_sum += ord(char)
    if (word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u" or word[0] =="y" or
        word[0] == "A" or word[0] == "E" or word[0] == "I" or word[0] == "O" or word[0] == "U" or word[0] == "Y"):
        ascii_sum *= len(word)
    else:
        ascii_sum = floor(ascii_sum / len(word))

    if ascii_sum > max_word_power:
        max_word_power = ascii_sum
        most_powerful_word = word

print(f"The most powerful word is {most_powerful_word} - {max_word_power}")



