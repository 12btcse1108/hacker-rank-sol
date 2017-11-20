
# coding: utf-8

# In[15]:

def anagram(str1, str2):
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()
    
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
    
anagram('aaab','bba')


# In[25]:

def anagram2(str1,str2):
    
    d = {}
    
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()
    
    if len(str1) != len(str2):
        return False
    
    for item in str1:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
            
    for item in str2:
        if item in d:
            d[item] -= 1
        else:
            d[item] = 1
            
    for item in d:
        if d[item] != 0:
            return False
    
    return True
            
    
anagram2('Clint Eastwood', 'old west action')   
    


# In[ ]:



