a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

if a <= b and a <= c:
    print("Min is", a)
elif b <= a and b <= c:
    print("Min is", b)
else:
    print("Min is", c)
