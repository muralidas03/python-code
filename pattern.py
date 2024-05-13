# num= int(input("Enter the number of row: "))
# for i in range(1,num+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# """
# *
# * *
# * * *
# * * * * """
# num= int(input("Enter the number of row: "))
# for i in range(num,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# """
# * * * *
# * * *
# * *
# *
# """
# num= 4
# for i in range(0,num):
#     for j in range(0,num-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print(i,end=" ")
#     print()
#
# """
#    *
#   * *
#  * * *
# * * * *
# """
num= int(input("Ente the number of row : "))
for i in range(num):
    print(" " * i, end="")
    for j in range(i+1):
        print(i,end=" ")
    print()
num = int(input("Enter a number: "))

for i in range(num):
    print(" " * i, end="")
    for j in range(i+1):
        print(i, end=" ")
    print()