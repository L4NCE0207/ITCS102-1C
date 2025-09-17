print("Hello, welcome to Multiplication Table Maker")

number = int(input("Enter a number: "))
print("Multiplication table for", number)

for x in range(1, 11):
    print(number, "x", x, "=", number * x)