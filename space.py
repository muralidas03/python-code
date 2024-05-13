str=input("Enter a str ;")
n=len(str)
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j or i+j==n-1 or i==0 or i==n-1 :
            print(str[i],end=" ")
        else:
            print(" ",end=" ")
    print()

