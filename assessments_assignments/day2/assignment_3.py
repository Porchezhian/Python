products = [
    {"pid": 1, "name": "pen", "cost": 45, "brand": "reynolds", "category": "stationary", "rating": 5, "discount": 2},
    {"pid": 2, "name": "t-shirt", "cost": 500, "brand": "ruggers", "category": "clothing", "rating": 4, "discount": 20},
    {"pid": 3, "name": "mobile", "cost": 30000, "brand": "oneplus", "category": "electronics", "rating": 5, "discount": 5},
    {"pid": 4, "name": "shoe", "cost": 3000, "brand": "reebok", "category": "clothing", "rating": 4.5, "discount": 10},
    {"pid": 5, "name": "belt", "cost": 250, "brand": "bata", "category": "clothing", "rating": 3.5, "discount": 2}
]

print("1. sort by cost - low to high")
print("2. sort by cost - high to low")
print("3. sort by rating")
print("4. sort by discount - low to high")
print("5. sort by discount - high to low")

choice = int(input("Enter an option: ")) - 1
print("\n")

options = [{"option":"cost", "reverse": False},
           {"option":"cost", "reverse": True},
           {"option":"rating", "reverse": True},
           {"option":"discount", "reverse": False},
           {"option":"discount", "reverse": True}]

products.sort(key= lambda el: el[options[choice]["option"]], reverse=options[choice]["reverse"])
for product in products:
    print("pid: {pid}\nname: {name}\ncost:{cost}\nbrand:{brand}\ncategory:{category}\nrating: {rating}\ndiscount: {discount}".format(**product))
    print("\n")