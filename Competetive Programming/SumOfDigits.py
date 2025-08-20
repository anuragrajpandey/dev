N = int(input("Enter a number: "))
total = 0
if N < 0:
    N = -N
while N != 0:
    digit = N % 10
    total += digit
    N //= 10
print("Sum of digits:", total)