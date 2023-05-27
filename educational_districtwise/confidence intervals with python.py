#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from scipy import stats


# In[4]:


file_path = r"C:\Users\Lu LIANG\Desktop\data_clean\data_clean\educational_districtwise\education_districtwise.csv"

education_districtwise = pd.read_csv( r"C:\Users\Lu LIANG\Desktop\data_clean\data_clean\educational_districtwise\education_districtwise.csv")

enducational_districtwise = education_districtwise.dropna()


# In[6]:


sampled_data = education_districtwise.sample(n = 50, replace =True, random_state = 31208) 
sampled_data


# In[8]:


sample_mean = sampled_data ['OVERALL_LI'].mean()
sample_mean


# In[9]:


estimated_standard_error = sampled_data['OVERALL_LI'].std()/np.sqrt(sampled_data.shape[0])


# In[13]:


stats.norm.interval(confidence = 0.95, loc = sample_mean, scale = estimated_standard_error)


# the conclusion : confidence interval : 95 CI [71.4, 77.0]

# In[14]:


stats.norm.interval(confidence = 0.99, loc = sample_mean, scale = estimated_standard_error)


# the conclusion : confidence interval : 99 CI [71.4, 77.0]

# In[ ]:




