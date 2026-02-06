def multiplication_table (n):
    for i in range (1,11):
        print( n * i)

def sum_of_numbers (n):
    total = 0
    for i in range (1,n+1):
        total = total + i
    return total 
    
n = int(input("Enter your number"))
    
print ("Select operation.")
print("1. Multiplication table")
print("2. Sum of n numbers.")

operation = int(input( "Enter operation"))
if operation == 1 :
    multiplication_table(n)
elif operation == 2:
    print(sum_of_numbers(n))
else:
    print("Invalid input")
       
