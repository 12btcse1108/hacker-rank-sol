
# coding: utf-8

# In[50]:

def pair_sum(arr, k):
    l = []
    s = set()
    arr_length = len(arr)
    for i in range(arr_length-1):
        for j in range(i,(arr_length-1)):
            new_k = arr[i] + arr[j]
            if new_k == k:
                s.add((arr[i],arr[j]))
    t = list(s)
    print("\n".join(map(str,t)))    
    
pair_sum([1, 5, 7, -1, 5],6)


# In[40]:

def pair_sum2(arr,k):
    seen = set()
    output = set()
    if len(arr) <= 1:
        return "array must contain 2 elements"
    for item in arr:
        target = item - k
        if target not in arr:
            seen.add(item)
        else:
            output.add((max(target,item),min(target,item)))
    print("\n".join(map(str,list(output))))

pair_sum2([1, 5, 7, -1, 5],6)


# In[ ]:



