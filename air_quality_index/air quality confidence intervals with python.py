#!/usr/bin/env python
# coding: utf-8

# The Air Quality Index (AQI) is the Environmental Protection Agency's index for reporting air quality. A value close to 0 signals little to no public health concern, while higher values are associated with increased risk to public health. The United States is considering a new federal policy that would create a subsidy for renewable energy in states observing an average AQI of 10 or above.
# 
# You've just started your new role as a data analyst in the Strategy division of Ripple Renewable Energy (RRE). RRE operates in the following U.S. states: California, Florida, Michigan, Ohio, Pennsylvania, Texas. You've been tasked with constructing an analysis which identifies which of these states are most likely to be affected, should the new federal policy be enacted.
# 
# Your manager has requested that you do the following for your analysis:
# 
# Provide a summary of the mean AQI for the states in which RRE operates.
# Construct a boxplot visualization for AQI of these states using seaborn.
# Evaluate which state(s) may be most affected by this policy, based on the data and your boxplot visualization.
# Construct a confidence interval for the RRE state with the highest mean AQI.

# In[1]:


# Import relevant packages.

### YOUR CODE HERE ###

import pandas as pd
import numpy as np


# In[3]:


# Use read_csv() to import the data.

### YOUR CODE HERE ###

file_path = r"C:\Users\Lu LIANG\Desktop\data_clean\data_clean\air_quality_index\c4_epa_air_quality.csv"

aqi = pd.read_csv( r"C:\Users\Lu LIANG\Desktop\data_clean\data_clean\air_quality_index\c4_epa_air_quality.csv")


# In[4]:


# Explore the `aqi` DataFrame.

### YOUR CODE HERE ###

print("Use describe() to summarize AQI")
print(aqi.describe(include='all'))


# In[5]:


print(aqi['state_name'].value_counts())


# In[6]:


# Create a list of RRE states.

rre_states = ['California','Florida','Michigan','Ohio','Pennsylvania','Texas']

# Subset `aqi` to only consider these states.

aqi_rre = aqi[aqi['state_name'].isin(rre_states)]

# Find the mean aqi for each of the RRE states.

aqi_rre.groupby(['state_name']).agg({"aqi":"mean","state_name":"count"}) #alias as aqi_rre


# Construct a boxplot visualization for the AQI of these states
# 

# In[7]:


# Import seaborn as sns.

import seaborn as sns


# In[8]:


sns.boxplot(x=aqi_rre["state_name"],y=aqi_rre["aqi"])


# California: The mean and a signficant portion of the boxplot range over 10.
# Michigan: While the mean is below 10, the boxplot ranges above 10.

# Construct a confidence interval for the RRE state with the highest mean AQI
# 

# In[11]:


aqi_ca = aqi[aqi['state_name']=='California']

sample_mean = aqi_ca['aqi'].mean()
sample_mean


# In[12]:


confidence_level = 0.95
confidence_level


# In[13]:


z_value = 1.96


# In[14]:


standard_error = aqi_ca['aqi'].std() / np.sqrt(aqi_ca.shape[0])
print("standard error:")
print(standard_error)


# In[15]:


margin_of_error = standard_error * z_value
print("margin of error:")
print(margin_of_error)


# In[16]:


# Calculate your confidence interval (upper and lower limits).

upper_ci_limit = sample_mean + margin_of_error
lower_ci_limit = sample_mean - margin_of_error
(lower_ci_limit, upper_ci_limit)


# What findings would you share with others?
# 
# Present this notebook to convey the analytical process and describe the methodology behind constructing the confidence interval.
# Convey that a confidence interval at the 95% level of confidence from this sample data yielded [10.36 , 13.88], which provides the interpretation "given the observed sample AQI measurements, there is a 95% confidence that the population mean AQI for California was between 10.36 and 13.88. This range is notably greater than 10."
# Share how varying the confidence level changes the interval. For example, if you varied the confidence level to 99%, the confidence interval would become [9.80 , 14.43].

# In[ ]:




