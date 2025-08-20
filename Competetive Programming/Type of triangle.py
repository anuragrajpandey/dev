a = int(input("Enter angle 1: "))
b = int(input("Enter angle 2: "))
c = int(input("Enter angle 3: "))

if a + b + c == 180:
    if a == 90 or b == 90 or c == 90:
        print("Right Triangle")
    elif a > 90 or b > 90 or c > 90:
        print("Obtuse Triangle")
    else:
        print("Acute Triangle")
else:
    print("Not a triangle")
