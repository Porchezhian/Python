#star patterns
num = int(input("Enter the no.of rows: "))
for i in range(1, num+1):
    print("*"*i)
print("\n")

for i in range(num, 0, -1):
    print("*"*i)
print("\n")

for i in range(num, 0, -1):
    print(" "*(num-i),  "*"*i)
print("\n")

for i in range(1, num+1):
    print(" "*(num-i), "*"*i)
print("\n")

for i in range(1, num+1):
    print(" "*(num-i), "* "*i)
print("\n")

#word pattern
data = input("Enter the string: ")
for i in range(1, len(data)+1):
    print(" "*(len(data)-i), data[0:i])

#factorial
number = int(input("Enter the number: "))
fac = 1
for i in range(number, 1, -1):
    fac = fac * i
print(fac)

#fibanocci
number = int(input("Enter the number: "))
f = [0, 1]
for i in range(number-2):
    l = len(f)
    f.append(f[l-1] + f[l-2])
print(f)