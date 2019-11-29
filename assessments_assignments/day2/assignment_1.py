#non secure
count = 0
def func():
    global count
    count = count + 1

for i in range(3):
    func()

print("Non closure:",count)

#-----------------------
#secure - this is called closure
def outer():
    c = 0
    def inner():
        nonlocal c
        c = c + 1
    def get():
        nonlocal c
        print("Closure:",c)
    return [inner, get]

test = outer()
test[0]()
test[0]()
test[0]()
test[0]()
test[0]()
test[1]()
