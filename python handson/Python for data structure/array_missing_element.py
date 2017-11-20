
# coding: utf-8

# In[16]:

def array_missing(arr1, arr2):
    new_arr = []
    for item in arr1:
        if item in arr2:
            arr2.remove(item)
        else:
            new_arr.append(item)
    return ("\t".join(map(str,new_arr)))
            


# In[17]:

def array_missing2(arr1,arr2):
    arr1.sort()
    arr2.sort()
    for i,j in zip(arr1,arr2):
        if i != j:
            return i
    return arr1[-1]



# In[19]:

import collections
def array_missing3(arr1,arr2):
    d = collections.defaultdict(int)
    
    for item in arr2:
        d[item] += 1
    
    for item in arr1:
        if d[item] == 0:
            return item
        else:
            d[item] -=1
            
print(array_missing([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]))


# In[ ]:



