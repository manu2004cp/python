'''arr=[59,89,9,56,78,34,45,]
largest =0
for i in arr:
    if i > largest:
       largest=i
    print(largest)'''

'''n=10
a=1
b=0
for i in range(n):
    print(a) 
    a,b=b,(a+b);'''
'''n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact)'''
start=0
end=len(arr)-1
while start < end:
arr[start],arr[end],=arr[end],arr[start]
end=end-1
print(arr)

