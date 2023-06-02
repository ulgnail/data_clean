#!/usr/bin/env python
# coding: utf-8

# Throughout this notebook, we will use the normal distribution to model our data. We will also compute z-scores to find any outliers in our data.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm


# In[8]:


file_path = r"C:\Users\Lu LIANG\Desktop\data_clean\data_clean\educational_districtwise\education_districtwise.csv"

df = pd.read_csv( r"C:\Users\Lu LIANG\Desktop\data_clean\data_clean\educational_districtwise\education_districtwise.csv")


# The first step in trying to model your data with a probability distribution is to plot a histogram. This will help you visualize the shape of your data and determine if it resembles the shape of a specific distribution.

# In[10]:


df['OVERALL_LI'].hist()


# The histogram shows that the distribution of the literacy rate data is bell-shaped and symmetric about the mean. The mean literacy rate, which is around 73%, is located in the center of the plot.
# 
# Since the normal distribution seems like a good fit for the district literacy rate data, we can expect the empirical rule to apply relatively well. Recall that the empirical rule says that for a normal distribution:
# 
# 68% of the values fall within +/- 1 SD from the mean
# 95% of the values fall within +/- 2 SD from the mean
# 99.7% of the values fall within +/- 3 SD from the mean
# 

# In[12]:


mean_overall_li = df['OVERALL_LI'].mean()
mean_overall_li


# In[13]:


std_overall_li = df['OVERALL_LI'].std()
std_overall_li


# In[19]:


#### tells the computer to decide if each value in the OVERALL_LI column is between the lower limit and upper limit.

lower_limit = mean_overall_li - 1 * std_overall_li
upper_limit = mean_overall_li + 1 * std_overall_li
((df['OVERALL_LI'] >= lower_limit) & (df['OVERALL_LI'] <= upper_limit)).mean()


# In[22]:


#### compute the actual percentage of district literacy rates that fall within +/- 2 SD from the mean 

lower_limit = mean_overall_li - 2 * std_overall_li
upper_limit = mean_overall_li + 2 * std_overall_li
((df['OVERALL_LI'] >= lower_limit) & (df['OVERALL_LI'] <= upper_limit)).mean()


# In[24]:


#### compute the actual percentage of district literacy rates that fall within +/- 3 SD from the mean

lower_limit = mean_overall_li - 3 * std_overall_li
upper_limit = mean_overall_li + 3 * std_overall_li
((df['OVERALL_LI'] >= lower_limit) & (df['OVERALL_LI'] <= upper_limit)).mean()


# Our values of 61.9%, 88.9%, and 92.3% are very close to the values the empirical rule suggests: roughly 68%, 95%, and 99.7%，but a  little bit lowrer.
# 
# This could indicate that the distribution of the dataset has some slight skewness or outliers, causing the actual distribution of the dataset to deviate slightly from the ideal normal distribution. However, since only a few data points are provided, we cannot determine the true distribution of the dataset. Further analysis and more data points may be required for a more accurate assessment.

# In[25]:


df['Z_SCORE'] = stats.zscore(df['OVERALL_LI'])
df


# In[27]:


df[(df['Z_SCORE'] > 3) | (df['Z_SCORE'] < -3)]


# However, no ouliter was funded. 
# 

# In[ ]:




