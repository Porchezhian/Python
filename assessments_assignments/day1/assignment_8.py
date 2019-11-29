#factorial
number = int(input("Enter the number: "))
fac = 1
for i in range(number, 1, -1):
    fac = fac * i
print(fac)
