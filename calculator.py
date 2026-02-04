print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
option = int(input("Enter operation"))
num1 =int(input("Enter first number"))
num2 =int(input("Enter second number"))
if option == 1:
    add = num1 + num2
    print("Your number is {}".format(add))
elif option == 2:
    subtract = num1 - num2
    print("Your number is {}".format(subtract))
elif option == 3:
    multiply = num1 * num2
    print("Your number is {}".format(multiply))
elif option == 4:
    divide = num1 // num2
    print("Your number is {}".format(divide))
else :
    print ("Invalid input. Please enter in 1, 2, 3, 4.")
