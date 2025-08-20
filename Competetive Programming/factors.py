N = int(input("Enter a number: "))
count = 0 
if N == 0:
    count = 1
else:
    while N !=0:
        N //= 10
        count +=1
        print ("The Number Of Digits: ", count)