'''lst=[1,2,3,5]
emp_lst=[]
for x in lst:
    if x%2==1:
        emp_lst.append(x)
print(emp_lst)'''

'''lst=[1,2,3,5]
print([x for x in lst if x%2==1])'''

'''lst=[1,2,3,5]
print(["odd" if x%2==1 else"even"for x in lst])'''

'''val=[[1,2,3,5],[7,8,9,4]]
print([y for x in val for y in x if y%2==1])'''        


'''val=[[1,2,3,5],[7,8,9,4]]
for x in val:
    print(sum(x))'''

for x in [[1,2,3,5],[7,8,9,4]]:
    sum=0
    for y in x:
        sum=sum+y
    print(sum)
