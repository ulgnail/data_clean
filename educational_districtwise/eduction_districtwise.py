#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[10]:


file_path = r"C:\Users\Lu LIANG\Desktop\dataclean\education_districtwise.csv"

df = pd.read_csv( r"C:\Users\Lu LIANG\Desktop\dataclean\education_districtwise.csv")


# In[12]:


df.head(10)


# In[16]:


row_count = len(df)
print(row_count)


# In[13]:


df['OVERALL_LI'].describe()


# In[17]:


df['STATNAME'].describe()


# In[21]:


range_overall_li = df['OVERALL_LI'].max() - df['OVERALL_LI'].min()
range_overall_li


# In[ ]:




