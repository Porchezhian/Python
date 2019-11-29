
year = int(input("Enter the year"))

if year % 400 == 0:
    print("Leap")
elif year/100 == 0:
    print("Not Leap")
elif year % 4 == 0:
    print("Leap")
else:
    print("Not Leap")