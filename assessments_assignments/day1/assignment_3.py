
date = int(input("Enter a date in november"))
result = (date % 7)-1
day = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
if date<1 or date>30:
    print("Invalid")
else:
    print(day[result])