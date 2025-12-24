movie_name = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
percentage = int(input())

ticket_price = tickets * ticket_price
income = ticket_price * days

cinema_percentage = (income * percentage) / 100
income -= cinema_percentage

print(f"The profit from the movie {movie_name} is {income:.2f} lv.")