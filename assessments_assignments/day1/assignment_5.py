number = int(input("Enter a number"))
i=2
while i <= number/2:
    if number % i == 0:
        print("Not a prime")
        break
    i = i + 1
else:
    print("Prime")