#Square
n = int(input("Enter the number of row : "))
for i in range(n):
    for j in range(n):
        print("*",end=' ')
    print()
# increasing triangle
n = int(input("Enter the number of row : "))
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    print()
#decreasing trangle
n = int(input("Enter the number of row : "))
for i in range(n):
    for j in range(i,n):
        print("*",end=' ')
    print()