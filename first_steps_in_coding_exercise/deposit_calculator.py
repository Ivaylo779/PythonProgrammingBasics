deposited_sum = float(input())
deposit_deadline = int(input())
annual_interest_rate = float(input())

sum = deposited_sum + deposit_deadline * ((deposited_sum * annual_interest_rate) / 100 / 12 )

print(sum)