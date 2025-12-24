ascii_sum = 0
iteration = 0
max_ascii_score = 0
best_movie = ""

for movie in range(1, 8):
    iteration += 1
    ascii_sum = 0
    movie_name = input()
    if movie_name == "STOP":
        break

    for char in movie_name:
        ascii_sum += ord(char)

    for char in movie_name:
        if 'a' <= char <= 'z':
            ascii_sum -= len(movie_name) * 2
        elif 'A' <= char <= 'Z':
            ascii_sum -= len(movie_name)

    if ascii_sum > max_ascii_score:
        max_ascii_score = ascii_sum
        best_movie = movie_name

    if iteration == 7:
        print("The limit is reached.")
        break

print(f"The best movie for you is {best_movie} with {max_ascii_score} ASCII sum.")