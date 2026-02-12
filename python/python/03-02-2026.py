'''nums=[5,2,9,1]
n=len(nums)
for i in range(n):
 for j in range(0,n-i-1):
    if nums[j]>nums[j+1]:
        # swap
        nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums) '''

'''lst=[1,3,4]
emp_lst=[]
for x in lst:
    emp_lst.append((x**2))
print(emp_lst)'''

'''print([x**3 for x in [1,3,4]])'''

a=12
b=45
result=a+b
print(result)
