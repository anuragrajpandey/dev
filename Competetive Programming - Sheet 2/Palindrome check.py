a = int(input("Enter number: "))
temp = a
rev = 0
while a > 0:
    rev = rev * 10 + (a % 10)
    a //= 10

if temp == rev:
    print("Yes, Palindrome")
else:
    print("No, Not Palindrome")
