products = [
    {"pid": 1, "name": "pen", "cost": 45, "brand": "reynolds", "category": "stationary", "rating": 5, "discount": 2},
    {"pid": 2, "name": "t-shirt", "cost": 500, "brand": "ruggers", "category": "clothing", "rating": 4, "discount": 20},
    {"pid": 3, "name": "mobile", "cost": 30000, "brand": "oneplus", "category": "electronics", "rating": 5, "discount": 5},
    {"pid": 4, "name": "shoe", "cost": 3000, "brand": "reebok", "category": "clothing", "rating": 4.5, "discount": 10},
    {"pid": 5, "name": "belt", "cost": 250, "brand": "bata", "category": "clothing", "rating": 3.5, "discount": 2}
]

print("1. Filter by category")
print("2. Filter by name")
print("3. Filter by brand")

option = int(input("Enter an option: ")) - 1
print("\n")

options = [{"option":"category"}, {"option":"name"}, {"option":"brand"}]
category = input("Enter the {0}: ".format(options[option]["option"]))
newlist = filter(lambda el: el[options[option]["option"]] == category, products)
for product in newlist:
    print("pid: {pid}\nname: {name}\ncost:{cost}\nbrand:{brand}\ncategory:{category}\nrating: {rating}\ndiscount: {discount}".format(**product))
    print("\n")