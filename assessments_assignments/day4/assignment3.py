import re

number = input("Enter your mobile number: ")
pattern = "^[0-9]{10}$"
match = re.search(pattern, number)
if match:
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")