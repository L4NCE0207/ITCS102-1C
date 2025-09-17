number = eval(input("Input a nnumber ---> "))
factorial = 1
for x in range(number, 0, -1):
    factorial *= x
print("The factorial os ",number, "is",factorial)