import os
import time
import sys

# ----------------------- HELPER FUNCTIONS -----------------------
def clear():
    """Clear screen (works on Windows and Unix-like)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(msg="Press Enter to continue..."):
    """Pause execution."""
    input(msg)

# ----------------------- WELCOME SEQUENCE -----------------------
clear()
print("------ WELCOME TO FRANCISCO'S PYTHON COMPILER -------\n")
name_input = input("Hello user! What's your name? ---> ").strip()
use_name = input(f"Hello there {name_input} do you want see my works?(yes/no) ---> ").strip().lower()
if use_name == "yes" and name_input:
    name = name_input
elif use_name == "no":
    print("Program terminated. Goodbye!")
    sys.exit() 
else:
    name = "Student"

print(f"\nWelcome {name}! This program will show many Python examples like a first-year student would make.")
time.sleep(1.5)
clear()


while True:
    print("‿̩͙⊱༒︎━━━━━━━━━━━━━━━━━━﹙ ୨ 🎕 ୧﹚━━━━━━━━━━━━━━━━━━༒︎⊰‿̩͙\n")
    print("\tA - PRINT FUNCTION")
    print("\tB - DICTIONARY")
    print("\tC - FOR LOOP")
    print("\tD - EVAL FUNCTION")
    print("\tE - LOOP")
    print("\tF - LIST")
    print("\tG - INT FUNCTION")
    print("\tH - STRING CONCATENATION")
    print("\tI - EQUATIONS")
    print("\tJ - WHILE LOOP")
    print("\tK - IF STATEMENT")
    print("\tL - NESTED FOR LOOP")
    print("\n‿̩͙⊱༒︎━━━━━━━━━━━━━━━━━━﹙ ୨ 🎕 ୧﹚━━━━━━━━━━━━━━━━━━༒︎⊰‿̩͙")
    print("\nX- Exit Menu\n")
    select = input("Select what command should we run: ").lower()
    clear()

    
    if select == 'a':
        print("==== PRINT FUNCTION MENU ====")
        print("1 - Information")
        print("2 - Run code example")
        print("3 - Back to main menu")
        choice = input("Enter choice: ").strip()
        clear()
        if choice == '1':
            print("==== PRINT FUNCTION INFORMATION ====")
            print("The print() function displays information on the screen. You can print text, numbers, variables, or results of calculations.")
            print("Examples:")
            print("1. Printing strings: print('Hello World')")
            print("2. Printing numbers: print(123)")
            print("3. Printing variables: name = 'pedring'; print(name)")
            print("4. Printing expressions: print(2 + 3)")
            print("\nAdvanced:")
            print("- Using commas separates items with spaces: print('A', 'B', 'C')")
            print("- Using '+' to concatenate strings: print('Hello' + 'World')")
            print("- f-strings embed variables: print(f'Name: {name}, Age: {age}')")
            print("- Changing end character: print('Hello', end='!')")
            print("- Changing separator: print('A','B','C', sep='-')")
            pause()

        elif choice == '2':
            print("==== RUN PRINT() EXAMPLES ====")
            name_input = input("Enter your name: ")
            age_input = input("Enter your age: ")
            print(f"Hello {name_input}, you are {age_input} years old.")
            
            expr1 = eval(input("\nEnter a number to multiply x: "))
            expr2 = eval(input("Enter a number to multiply y: "))
            print(f"Result of {expr1} * {expr2} =", expr1 * expr2)
            pause()


    elif select == 'b':
        print("==== DICTIONARY MENU ====")
        print("1 - Information")
        print("2 - Run code example")
        print("3 - Back to main menu")
        choice = input("Enter choice: ").strip()
        clear()
        if choice == '1':
            print("==== DICTIONARY INFORMATION ====")
            print("A dictionary stores key:value pairs.")
            print("Keys must be unique; values can be any type.")
            print("Dictionaries are unordered but very useful for structured data.")
            print("You can add, update, remove, and access items easily using keys.")
            print("Example: student = {'name':'pedring', 'age':20}")
            print("Access: student['name'] -> 'pedring'")
            print("Update: student['age'] = 21")
            print("Add: student['course'] = 'BSIT'")
            print("Remove: student.pop('course')")
            pause()
        elif choice == '2':
            print("==== RUN DICTIONARY EXAMPLE ====")
            student = {"name": "Pedring", "age": 20, "course": "BSIT"}
            print("Initial dictionary:", student)
            student["age"] = input("Enter new age: ")
            student["gpa"] = 3.8
            print("Updated dictionary:", student)
            pause()

    
    elif select == 'c':
        print("==== FOR LOOP MENU ====")
        print("1 - Information")
        print("2 - Run code example")
        print("3 - Back to main menu")
        choice = input("Enter choice: ").strip()
        clear()
        if choice == '1':
            print("==== FOR LOOP INFORMATION ====")
            print("For loops are used to repeat a block of code for each item in a sequence such as a list, string, tuple, or range.")
            print("They are very useful when you know beforehand how many times you want the code to run, which helps reduce repetitive coding.")
            print("\nSYNTAX:")
            print("for variable in sequence:")
            print("    # code to execute for each item in the sequence")

            print("\nDETAILS:")
            print("- The 'variable' takes the value of each item in the sequence one by one.")
            print("- The sequence can be a list, tuple, string, range, or any iterable.")
            print("- You can nest for loops inside each other to work with multi-dimensional data structures.")
            print("- Loops can be combined with 'if' statements to filter items or perform conditional actions.")
            print("- Common loop control statements include 'break' (to exit the loop) and 'continue' (to skip the current iteration).")
            print("- Avoid infinite loops by ensuring the sequence is finite or using proper loop control.")

            print("\nEXAMPLES OF USAGE:")
            print("1) Iterating over a range of numbers: for i in range(1,6)")
            print("2) Iterating over a list of items: for item in ['apple', 'banana', 'cherry']")
            print("3) Iterating over characters in a string: for char in 'Python'")
            print("4) Iterating over dictionary keys: for key in {'name':'Alice','age':20}")

            print("\nNESTED LOOPS:")
            print("- Nested loops are used when working with multi-dimensional data, such as matrices or tables.")
            print("- Example: for i in range(3): for j in range(3): print(i, j)")
            print("- The inner loop runs completely for every iteration of the outer loop.")

            print("\nTIPS:")
            print("- Use for loops for sequences with a known number of iterations.")
            print("- Keep loops readable by properly indenting code blocks.")
            print("- Use loops with list comprehensions for concise and efficient code.")
            print("- Combine with break/continue to manage loop flow effectively.")

            pause()

        elif choice == '2':
            n = int(input("Enter a number n to print 1..n: "))
            for i in range(1, n + 1):
                print(i)
            pause()

    
    elif select == 'd':
        print("==== EVAL FUNCTION MENU ====")
        print("1 - Information")
        print("2 - Run code example")
        choice = input("Enter choice: ").strip()
        clear()
        if choice == '1':
            print("==== EVAL() INFORMATION ====")
            print("The eval() function takes a string as input and evaluates it as a Python expression.")
            print("It can handle arithmetic expressions, numbers, lists, tuples, dictionaries, function calls, and more.")
            print("\nSYNTAX:")
            print("eval(expression, globals=None, locals=None)")
            print("- 'expression' is a string containing a valid Python expression.")
            print("- 'globals' and 'locals' are optional dictionaries that define the global and local variables available during evaluation.")

            print("\nEXAMPLES:")
            print("1) Simple arithmetic: eval('2 + 3') -> 5")
            print("2) Using variables: x = 10; eval('x * 2') -> 20")
            print("3) Evaluating a list: eval('[1, 2, 3]') -> [1, 2, 3]")
            print("4) Calling a function (if defined in scope): eval('my_func()')")

            print("\nCAUTION / WARNING:")
            print("- Never use eval() on input from untrusted sources. It can execute arbitrary Python code and may be a serious security risk.")
            print("- Safer alternatives for literals: ast.literal_eval() for evaluating strings that represent Python literals (numbers, lists, tuples, dicts).")

            print("\nTIPS:")
            print("- Use eval() mainly for learning, experimenting, or controlled environments.")
            print("- For user input in calculators, always sanitize or use safer methods.")
            print("- Combine with try/except to handle invalid expressions gracefully.")


        elif choice == '2':
            expr = input("Enter arithmetic expression: ")
            try:
                print("Result:", eval(expr))
            except Exception as e:
                print("Error:", e)
            pause()

    
    elif select == 'e':
        print("==== LOOP MENU ====")
        print("1 - Information about loops")
        print("2 - Run code example")
        choice = input("Enter choice: ").strip()
        clear()
        if choice == '1':
            print("==== LOOP INFORMATION ====")
            print("Loops are used to repeatedly execute a block of code until a condition is met or for each item in a sequence.")
            print("They help automate repetitive tasks, reduce code duplication, and make programs more efficient.")
            print("\nTYPES OF LOOPS IN PYTHON:")
            print("1) for loop: Iterates over a sequence such as a list, string, tuple, or range.")
            print("   Syntax: for variable in sequence:\n              # code to execute")
            print("2) while loop: Repeats a block of code as long as a condition is True.")
            print("   Syntax: while condition:\n              # code to execute")

            print("\nLOOP CONTROL STATEMENTS:")
            print("- break: Immediately exits the loop.")
            print("- continue: Skips the current iteration and moves to the next one.")
            print("- pass: Does nothing, acts as a placeholder for future code.")

            print("\nEXAMPLES:")
            print("1) For loop over a list: for item in ['apple', 'banana'] -> executes code for each item.")
            print("2) While loop with counter:")
            print("   i = 1")
            print("   while i <= 5:")
            print("       print(i)")
            print("       i += 1")
            print("3) Using break:")
            print("   while True:")
            print("       input_val = input('Enter q to quit: ')")
            print("       if input_val == 'q':")
            print("           break")
            print("4) Using continue:")
            print("   for i in range(5):")
            print("       if i == 2:")
            print("           continue  # skips printing 2")
            print("       print(i)")

            print("\nTIPS:")
            print("- Use for loops when the number of iterations is known or iterating over sequences.")
            print("- Use while loops when the number of iterations depends on a condition.")
            print("- Always make sure the loop condition will eventually be False to avoid infinite loops.")
            print("- Loops can be nested to handle more complex logic or multi-dimensional data.")

            pause()

        elif choice == '2':
            for i in range(1, 11):
                print(f"Counting: {i}")
            pause()

    
    elif select == 'f':
        print("==== LIST MENU ====")
        print("1 - Information about lists")
        print("2 - Run code example")
        choice = input("Enter choice: ").strip()
        clear()
        if choice == '1':
            print("==== LIST INFORMATION ====")
            print("A list is an ordered and changeable collection of items in Python.")
            print("Lists can store any data type and can be modified anytime.")
            print("\nExample:")
            print("fruits = ['apple', 'banana', 'cherry']")

            print("\nACCESSING ITEMS:")
            print("fruits[0] -> 'apple'")
            print("fruits[-1] -> 'cherry'")

            print("\nADDING ITEMS:")
            print("fruits.append('orange')")
            print("fruits.insert(1, 'grapes')")

            print("\nREMOVING ITEMS:")
            print("fruits.pop(1)  # removes 'banana'")
            print("fruits.remove('apple')")
            print("fruits.clear()")

            print("\nMODIFYING ITEMS:")
            print("fruits[0] = 'mango'")

            print("\nCOMMON LIST FUNCTIONS:")
            print("len(fruits), fruits.sort(), fruits.reverse()")
            print("fruits.count('apple'), fruits.index('banana')")

            print("\nLOOP EXAMPLE:")
            print("for item in fruits: print(item)")

            pause()

        elif choice == '2':
            fruits = ['apple', 'banana', 'cherry']
            print("Initial list:", fruits)
            fruits.append('orange')
            print("After adding orange:", fruits)
            fruits.pop(1)
            print("After removing second item:", fruits)
            pause()

    
    elif select == 'g':
        print("==== INT FUNCTION MENU ====")
        print("1 - Information about int()")
        print("2 - Run code example")
        choice = input("Enter choice: ").strip()
        clear()
        if choice == '1':
            print("==== INT() INFORMATION ====")
            print("The int() function converts a value into an integer (whole number).")
            print("It can convert floats, numeric strings, and boolean values to integers.")
            print("\nExamples:")
            print("int(3.9) -> 3          # removes decimal part")
            print("int('10') -> 10        # converts string to integer")
            print("int(True) -> 1         # True becomes 1, False becomes 0")

            print("\nNOTES:")
            print("- Strings must contain valid numbers, or int() will cause an error.")
            print("- Useful for converting input() values which are always strings.")

            pause()

        elif choice == '2':
            x = input("Enter a number (string or float): ")
            print("Converted to integer:", int(float(x)))
            pause()

    
    elif select == 'h':
        print("==== STRING CONCATENATION MENU ====")
        print("1 - Information")
        print("2 - Run code example")
        choice = input("Enter choice: ").strip()
        clear()
        if choice == '1':
            print("==== STRING CONCATENATION INFORMATION ====")
            print("String concatenation means joining two or more strings together.")
            print("In Python, this is usually done using the + operator.")

            print("\nExample:")
            print("'Hello' + ' ' + 'World' -> 'Hello World'")

            print("\nYou can combine variables and strings too:")
            print("name = 'lance'")
            print("message = 'Hello ' + name")
            print("Result: 'Hello lance'")

            print("\nNOTES:")
            print("- Only strings can be concatenated. Numbers must be converted using str().")
            print("  Example: 'Age: ' + str(18)")
            print("- Concatenation is useful for greetings, messages, and building long text.")

            pause()

        elif choice == '2':
            a = input("write 'i am ' ---> ")
            b = input("write your name ---> ")
            print("Concatenated:", a + b)
            pause()


    elif select == 'i':
        print("==== EQUATIONS MENU ====")
        print("1 - Information")
        print("2 - Run code example")
        choice = input("Enter choice: ").strip()
        clear()

        if choice == '1':
            print("==== EQUATIONS INFORMATION ====")
            print("Python allows you to solve arithmetic equations using operators:")
            print("  +  -> addition")
            print("  -  -> subtraction")
            print("  *  -> multiplication")
            print("  /  -> division (always returns float)")
            print("  ** -> exponentiation (power)")
            print("  %  -> modulo (remainder after division)")
            print("\nExample equations:")
            print("  2 + 3 -> 5")
            print("  5 * 6 -> 30")
            print("  2 ** 3 -> 8")
            print("  10 % 3 -> 1")
            print("\nYou can also combine operators to form more complex expressions:")
            print("  2 + 3 * 4 -> 14 (Python follows the order of operations)")
            print("\nUse Python to quickly evaluate arithmetic expressions and equations.")
            pause()

        elif choice == '2':
            print("==== RUN EQUATION EXAMPLE ====")
            print("Type any arithmetic equation using +, -, *, /, **, %")
            print("Example: 2 + 3 * 4")
            try:
                eq = input("Enter your equation: ")
                result = eval(eq)
                print("Result:", result)
            except Exception as e:
                print("Error! Make sure you enter a valid equation.")
                print("Details:", e)
            pause()

    
    elif select == 'j':
        print("==== WHILE LOOP MENU ====")
        print("1 - Information")
        print("2 - Run code example")
        choice = input("Enter choice: ").strip()
        clear()
        if choice == '1':
            print("==== WHILE LOOP INFORMATION ====")
            print("While loops repeatedly execute a block of code as long as a condition is True.")
            print("\nSyntax:")
            print("  while condition:")
            print("      # code to execute repeatedly")
            print("\nKey points:")
            print("- Make sure the condition eventually becomes False, otherwise you'll get an infinite loop.")
            print("- You can use break to exit the loop early or continue to skip to the next iteration.")
            print("- Commonly used for counters, menus, or repeated user input until a condition is met.")
            print("\nExample:")
            print("  count = 0")
            print("  while count < 5:")
            print("      print(count)")
            print("      count += 1")
            pause()
        
        elif choice == '0':
            break

        elif choice == '2':
            print("==== RUN WHILE LOOP EXAMPLE ====")
            print("This loop will print numbers from 0 to 4.")
            count = 0
            while count < 5:
                print("Count =", count)
                count += 1
            print("\nYou can modify the condition or counter to change the loop behavior.")
            pause()


    
    elif select == 'k':
        print("==== IF STATEMENT MENU ====")
        print("1 - Information")
        print("2 - Run code example")
        choice = input("Enter choice: ").strip()
        clear()
        if choice == '1':
            print("==== IF STATEMENT INFORMATION ====")
            print("If statements allow your program to make decisions based on conditions.")
            print("The code inside the if block only runs if the condition is True.")
            print("\nSyntax:")
            print("  if condition:")
            print("      # code to execute if condition is True")
            print("  elif another_condition:")
            print("      # code if the previous condition was False and this is True")
            print("  else:")
            print("      # code if all previous conditions are False")
            print("\nExample:")
            print("  age = 20")
            print("  if age >= 18:")
            print("      print('You are an adult')")
            print("  else:")
            print("      print('You are a minor')")
            print("\nNotes:")
            print("- Conditions can use operators like ==, !=, <, >, <=, >=.")
            print("- You can combine conditions using and, or, not.")
            pause()

        elif choice == '2':
            print("==== RUN IF STATEMENT EXAMPLE ====")
            try:
                age = int(input("Enter your age: "))
                if age >= 18:
                    print("You are an adult.")
                elif age < 0:
                    print("Invalid age! Age cannot be negative.")
                else:
                    print("You are a minor.")
            except ValueError:
                print("Invalid input! Please enter a number.")
            pause()

    
    elif select == 'l':
        print("==== NESTED FOR LOOP MENU ====")
        print("1 - Information")
        print("2 - Run code example")
        choice = input("Enter choice: ").strip()
        clear()
        if choice == '1':
            print("==== NESTED FOR LOOP INFORMATION ====")
            print("Nested loops are loops inside another loop. They are often used for tables, grids, or multi-dimensional structures like matrices.")
            print("\nSyntax:")
            print("  for outer_variable in outer_sequence:")
            print("      for inner_variable in inner_sequence:")
            print("          # code to execute inside inner loop")
            print("\nExample:")
            print("  for i in range(3):")
            print("      for j in range(2):")
            print("          print(i, j)")
            print("\nNotes:")
            print("- The inner loop completes all its iterations for each iteration of the outer loop.")
            print("- Useful for working with 2D lists, patterns, or multi-level data.")
            pause()

        elif choice == '2':
            print("==== RUN NESTED FOR LOOP EXAMPLE ====")
            print("This loop prints all combinations of i and j from 1 to 3:")
            for i in range(1, 4):
                for j in range(1, 4):
                    print(f"i={i}, j={j}")
            print("\nYou can change the range or add more loops for more complex structures.")
            pause()

    
    elif select == 'x':
        print(f"Goodbye, {name}!")
        break

    else:
        print("Invalid choice. Try again.")
        pause()
    clear()