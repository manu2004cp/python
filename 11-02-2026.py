'''#case 2
import copy
lst1=[[100,200],300,900]
print(lst1,"original copy")
lst2=copy.copy(lst1)#shallow copy
print(lst2,"copied from lst1")
lst2[0][0]=999
print(lst1,"after modification in dulpicate,and its original")
print(lst2,"after modification in dulpicate,and its duplicate")'''

'''#case 2
import copy
lst1=[[100,200],300,900]
print(lst1,"original copy")
lst2=copy.deepcopy(lst1)#shallow copy
print(lst2,"copied from lst1")
lst2[0][0]=999
print(lst1,"after modification in dulpicate,and its original")
print(lst2,"after modification in dulpicate,and its duplicate")'''

'''list
import time
lst=[1,2,23,55]
start=time.time()
print(23 in lst)
end=time.time()
print(end-start)'''


'''tuple
import time
tup=(1,2,23,55)
start=time.time()
print(23 in tup)
end=time.time()
print(end-start)'''


'''#list
import sys
lst=[1,2,23,55]
p=sys.getsizeof(lst)
print(p)'''

#tuple
import sys
tup=[1,2,23,55]
p=sys.getsizeof(tup)
print(p)

