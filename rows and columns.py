for row in range (5):
    for col in range (5):
        print("*" ,end=" ")
    print()


for row in range (5):
    for col in range (row):
        print("*",end= " ")
    print()


for row in range (1,6):
    for col in range (1, row + 1):
        print (col,end="") 
    print()


for col in range (1,6):
    for row in range (1, col + 1):
        print (row ,end="") 
    print()