#Right side triangle
n = int(input("Enter the number of row : "))
for i in range(n):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print()
n = int(input("Enter the number of row : "))
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n):
        print("*",end=' ')
    print()

n = int(input("Enter the number of row : "))
for i in range(n):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

n = int(input("Enter the number of row : "))
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
n = int(input("Enter the number of row : "))
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()