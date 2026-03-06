# Task 1 — Calculate Average
my_list=[]
for i in range (5):
    nums = int(input("Enter your numbers one at a time"))
    my_list.append(nums)
print(my_list)
total_sum = 0
for num in my_list:
    total_sum += num
average = total_sum / len(my_list)
print(f"The average is : {average}.")

# Task 2 — Above Average Filter. print all the number that are above average
print("Numbers greater than average:")
for num in my_list:
    if num > average:
        print(num)

#Task 3 — Find Smallest Number (No min())
smallest = my_list[0]

for num in my_list:
    if num < smallest:
        smallest = num
print("Smallest number:", smallest) 