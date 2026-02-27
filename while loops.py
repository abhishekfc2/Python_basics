# Task 1 : Number Counter

number = int(input(" Enter a number between 1 - 50"))
while number > 50 or number < 1:
    print("You entered wrong number. Try again")
    number = int(input(" Enter a number between 1 - 50"))
else :
    for i in range (number):
        print (i)
        i += 1
# corrected code by chat gpt
number = int(input("Enter a number: "))   # 👈 USER INPUT

count = 1
while count <= number:                    # 👈 LOOP USES THAT INPUT
    print(count)
    count += 1



# Task 2 : — Password system

password = 1234
p = (input("Enter your password"))
while p != password:
    print("wrong password.")
    p = input("Enter your password")

print ("Access granted")


#Task 3 — Menu loop

menu = ("""1.Say Hello 
2.Say Bye 
3.Exit""")
while True:
    print(menu)
    user_input = int(input("Enter choice: "))

    if user_input == 1:
        print("Hello")
    elif user_input == 2:
        print("Bye")
    elif user_input == 3:
        print("Exiting...")
        break
    else:
        print("Invalid input")