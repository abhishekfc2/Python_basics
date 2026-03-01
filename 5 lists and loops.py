# Task 1 — Sum of Even Numbers in a List

n = 5
numbers = []
even_numbers= []
for i in range (n):
    x = int(input("Enter the numbers one at a time"))
    numbers.append(x)
for number in (numbers):
    if number % 2 == 0:
        even_numbers.append(number)
e = sum(even_numbers)
print(f"Sum of even numbers is :{e}")

# Task 2 — Find the Largest Number

n=5
numbers =[]
for i in range(n):
    x = int(input("Enter the numbers one a at time"))
    numbers.append(x)
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
       largest_number = number
print(largest_number)

# Task 3 — Count Positives & Negatives

my_list =[3, -2, 7, -5, 0, 4]
positive_numbers = []
negative_numbers = []
for i in my_list:
    if i >= 0:
        positive_numbers.append(i)
    else :
        negative_numbers.append(i)      
a = len(positive_numbers)
b = len(negative_numbers)
print (f"""Positive numbers:{a}
Negative numbers:{b}""")