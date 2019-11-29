number = int(input("Enter a number"))
i = 2
factors = [1]
while i <= number/2:
    if number % i == 0:
        factors.append(i)
    i = i + 1
factors.append(number)
print("Factors: ", factors)
print("No.of factors: ", len(factors))
print("Sum of factors: ", sum(factors))

