class product:
    def __init__(self, pid, name, brand, category, cost, rating, discount):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.category = category
        self.cost = cost
        self.rating = rating
        self.discount = discount
    def func(self, option):
        keys = [{"option": self.category},
                {"option": self.name},
                {"option": self.brand}]
        return keys[option]["option"]
    def __str__(self):
        return "pid: {0}\nname: {1}\nbrand: {2}\ncategory: {3}\ncost: {4}\nrating: {5}\ndiscount: {6}\n\n"\
            .format(self.pid, self.name, self.brand, self.category, self.cost, self.rating, self.discount)

p1 = product(1, "t-shirt", "ruggers", "clothing", 700, 4.5, 20)
p2 = product(2, "shoe", "reebok", "clothing", 2800, 4.3, 10)
p3 = product(3, "mobile", "oneplus", "electronics", 30000, 4.7, 10)
p4 = product(4, "shirt", "ruggers", "clothing", 800, 4, 2)
p5 = product(5, "laptop", "HP", "electronics", 70000, 3.9, 0)
products = [p1, p2, p3, p4, p5]

print("1. Filter by category")
print("2. Filter by name")
print("3. Filter by brand")

option = int(input("Enter an option: ")) - 1
print("\n")
options = [{"option":"category"}, {"option":"name"}, {"option":"brand"}]
category = input("Enter the {0}: ".format(options[option]["option"]))
newlist = filter(lambda p: p.func(option) == category, products)

for product in newlist:
    print(product)


