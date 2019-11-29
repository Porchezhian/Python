import os, re
pattern = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
all = []
valid = []
for file in os.listdir():
    if file.endswith(".log"):
        with open(file,'r') as fo:
            data = fo.read()
            all.append(data)
print("All the emails:")
for i in all:
    print(i)
    match = re.search(pattern, i)
    if match:
        valid.append(i)
print("-------------")
print("Valid emails:")
for i in valid:
    print(i)
