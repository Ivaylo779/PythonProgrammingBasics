V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

pipe1 = P1 * H
pipe2 = P2 * H
total = pipe1 + pipe2
pipe1_percent = pipe1 / total * 100
pipe2_percent = pipe2 / total * 100
percentage = (total / V) * 100

if total <= V:
    print(f"The pool is {percentage:.2f}% full. Pipe 1: {pipe1_percent:.2f}%. "
           f"Pipe 2: {pipe2_percent:.2f}%."
)
else:
    diff = total - V
    print(f"For {H} hours the pool overflows with {diff:.2f} liters.")












