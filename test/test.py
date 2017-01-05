import time
print time.localtime()

name = "head first python"

def what_happen_here():

    # print(name)
    name = str(1)
    # global name
    # name = name + " is a great book!"
    print(name)

what_happen_here()
print(name)

for num in range(4):
    print(num)
