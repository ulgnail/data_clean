#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
from scipy import stats


# In[20]:


file_path = r"C:\Users\Lu LIANG\Desktop\data_clean\data_clean\educational_districtwise\education_districtwise.csv"

education_districtwise = pd.read_csv( r"C:\Users\Lu LIANG\Desktop\data_clean\data_clean\educational_districtwise\education_districtwise.csv")


# In[21]:


education_districtwise = education_districtwise.dropna()


# In[22]:


state21 = education_districtwise[education_districtwise['STATNAME'] == "STATE21"]


# In[23]:


state28 = education_districtwise[education_districtwise['STATNAME'] == "STATE28"]


# In[24]:


sampled_state21 = state21.sample(n=20, replace = True, random_state=13490)


# In[25]:


sampled_state28 = state28.sample(n=20, replace = True, random_state=39103)


# In[26]:


sampled_state21['OVERALL_LI'].mean()


# In[27]:


sampled_state28['OVERALL_LI'].mean()


# Based on the sample data, the observed difference between the mean district literacy rates of STATE21 and STATE28 is 6.2 percentage points (70.8% - 64.6%). 

# Conduct a hypothesis test
# 
# 1.   State the null hypothesis and the alternative hypothesis
# 2.   Choose a significance level
# 3.   Find the p-value 
# 4.   Reject or fail to reject the null hypothesis

# State the null hypothesis and the alternative hypothesis
# 𝐻0: There is no difference in the mean district literacy rates between STATE21 and STATE28
# 𝐻𝐴: There is a difference in the mean district literacy rates between STATE21 and STATE28

# Step 2: Choose a significance level
# standard level of 5%

# Step 3: Find the p-value

# In[28]:


stats.ttest_ind(a=sampled_state21['OVERALL_LI'], b=sampled_state28['OVERALL_LI'], equal_var=False)


# This means there is only a 0.64% probability that the absolute difference between the two mean district literacy rates would be 6.2 percentage points or greater if the null hypothesis is true. In other words, it’s highly unlikely that the difference in the two means is due to chance.

# conclusion:
# Since the p-value is extremely small (much smaller than the significance level of 5%), I reject the null hypothesis. I conclude that there is a statistically significant difference in the average total fare amount between customers who use credit cards and customers who use cash.

# In[ ]:





# In[ ]:




