
mark = int(input("Enter the mark"))

if mark<0 or mark>100:
    print("Invalid")
elif mark<40:
    print("Fail")
elif mark<=59:
    print("Third")
elif mark<=79:
    print("Second")
else:
    print("First")