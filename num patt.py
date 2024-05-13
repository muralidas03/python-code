# n= int(input("Enter the number of rows : "))
# p=1
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#     p+=1
#     print()
#
# #Right side triangle
# n = int(input("Enter the number of row : "))
# p=1
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print(p,end=" ")
#     p+=1
#     print()
#
# n = int(input("Enter the number of row : "))
# p=1
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=' ')
#     for j in range(i):
#         print(p,end=" ")
#     for j in range(i+1):
#         print(p,end=" ")
#     p=p+1
#     print()
#
# """Decrementing"""
# n= int(input("Enter the number of rows : "))
# p=n
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#     p-=1
#     print()
# """Row incrementing by 2"""
# n= int(input("Enter the number of rows : "))
# p=0
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#     p+=2
#     print()
# """IF ROW odd  Some Condition"""
# n= int(input("Enter the number of rows : "))
# for i in range(n):
#     for j in range(i+1):
#         if (i%2==0):
#             print("1",end=" ")
#         else:
#             print("2",end=" ")
#     print()
#
# """Dimond pattern  Incrementing"""
# n = int(input("Enter the number of row : "))
# p=1
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print(p,end=" ")
#     for j in range(i+1):
#         print(p,end=" ")
#     p+=1
#     print()
#
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print(p,end=" ")
#     for j in range(i,n):
#         print(p,end=" ")
#     p+=1
#     print()
#
# """Dimond pattern incrementing and decrementing"""
n = int(input("Enter the number of row : "))
p=1
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(p,end=" ")
    for j in range(i+1):
        print(p,end=" ")
    p+=1
    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(p,end=" ")
    for j in range(i,n):
        print(p,end=" ")
    p-=1
    print()

"""IF change column """
n = int(input("Enter the number of row : "))

for i in range(n):
    p = 1
    for j in range(i+1):
        print(p,end=' ')
        p+=1
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
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

