per = int(input("Enter percentage: "))

if per < 25:
    print("Grade: D")
elif per >= 25 and per < 45:
    print("Grade: C")
elif per >= 45 and per < 65:
    print("Grade: B")
elif per >= 65 and per < 85:
    print("Grade: A")
else:
    print("Grade: A+")
