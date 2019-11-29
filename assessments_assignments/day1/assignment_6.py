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
