nums=["01/19/2024 10:00:01", "01/09/2023 11:00:09","01/09/2023 11:00:01", "02/05/2024 12:00:01" ]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]<nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
print(nums)

class Solution:
    def sortArray(self,nums):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        print(nums)
s1=Solution()
list=[]
n=int(input("Enter a number You Want : "))
for i in range(n):
    list.append(int(input("Enter a number For a list : ")))
print(f"Non Shorted list is {list}")
s1.sortArray(list)