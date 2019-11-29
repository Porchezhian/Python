#fibanocci
number = int(input("Enter the number: "))
f = [0, 1]
for i in range(number-2):
    l = len(f)
    f.append(f[l-1] + f[l-2])
print(f)
