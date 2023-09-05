#!/usr/bin/env python
# coding: utf-8

# In[49]:


def isPhoneNumber(text):
    if len(text) !=14:
        return False
    for i in range(0,2):
        if not text[i].isdecimal():
            return False 
    if text[2] != ' ':
        return False
    for i in range (3,5):
            if not text[i].isdecimal():
                return False
    if text[5] != ' ':
        return False
    for i in range(6,8):
        if not text[i].isdecimal():
            return False
    if text[8] != ' ':
        return False
    for i in range (9,11):
        if not text[i].isdecimal():
            return False
    if text[11] !=' ':
        return False
    for i in range(12,14):
         if not text[i].isdecimal():
            return False 
    
    return True
        


# In[50]:


message = 'call me at 07 83 39 31 83 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+14]
    if isPhoneNumber(chunk):
        print ('Phone number found: '+ chunk)
print('Done')


# In[ ]:




