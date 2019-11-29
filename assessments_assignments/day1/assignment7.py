#word pattern
data = input("Enter the string: ")
for i in range(1, len(data)+1):
    print(" "*(len(data)-i), data[0:i])
