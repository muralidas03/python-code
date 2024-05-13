x=10
y=20

temp=x
x=y
y=temp
# print(temp,"This Is Temp Value After swaf")
print(x,"This Is X value After Swaf")
print(y,"This Is y value After Swaf")

x=200
y=300
x,y=y,x
print(x,y)

num=10
res=1
for i in range(num,1,-1):
    res=res*i
print(res)

fno=0
sno=1
print(fno,end=" ")
print(sno,end=" ")
res=fno+sno
while res<100:
    print(res,end=" ")
    fno=sno
    sno=res
    res=fno+sno
print()
"""Find Big Number """
x=[10,11,10,20,4001,5,8,9,4002]
big=0
for i in x:
    if big<i:
        big=i
    else:
        continue
print(big)

"""Give Element is Aval Or Not """
x=[10,11,12,13,14,15,16,122]
element=int(input("Enter A Element : "))
pos=-1
for i in range(len(x)):
    if element==x[i]:
        pos=i
if pos==-1:
    print("Element is Not Founded",pos)
else:
    print("Element positions is",pos)