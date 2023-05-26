#!/usr/bin/env python
# coding: utf-8

# Use Python to simulate random sampling and make a point estimate of a population mean based on the sample data
# 

# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm


# In[12]:


file_path = r"C:\Users\Lu LIANG\Desktop\data_clean\data_clean\educational_districtwise\education_districtwise.csv"

education_districtwise = pd.read_csv( r"C:\Users\Lu LIANG\Desktop\data_clean\data_clean\educational_districtwise\education_districtwise.csv")


# In[13]:


sampled_data = education_districtwise.sample(n=50, replace=True, random_state=31208)
sampled_data 


# In[17]:


estimate1 = sampled_data['OVERALL_LI'].mean()
estimate1


# In[18]:


estimate2 = education_districtwise['OVERALL_LI'].sample(n=50, replace=True, random_state=56810).mean()
estimate2


# In[21]:


estimate_list = []
for i in range (10000):
    estimate_list.append(education_districtwise['OVERALL_LI'].sample(n = 50, replace = True).mean())
estimate_df = pd.DataFrame(data = {'estimate':estimate_list})


# In[23]:


mean_sample_means = estimate_df['estimate'].mean()
mean_sample_means 


# In[25]:


population_mean = education_districtwise['OVERALL_LI'].mean()
population_mean


# In[26]:


plt.hist(estimate_df['estimate'], bins=25, density=True, alpha=0.4, label = "histogram of sample means of 10000 random samples")
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100) # generate a grid of 100 values from xmin to xmax.
p = stats.norm.pdf(x, mean_sample_means, stats.tstd(estimate_df['estimate']))
plt.plot(x, p,'k', linewidth=2, label = 'normal curve from central limit theorem')
plt.axvline(x=population_mean, color='g', linestyle = 'solid', label = 'population mean')
plt.axvline(x=estimate1, color='r', linestyle = '--', label = 'sample mean of the first random sample')
plt.axvline(x=mean_sample_means, color='b', linestyle = ':', label = 'mean of sample means of 10000 random samples')
plt.title("Sampling distribution of sample mean")
plt.xlabel('sample mean')
plt.ylabel('density')
plt.legend(bbox_to_anchor=(1.04,1))
plt.show()


# There are three key takeaways from this graph:
# 
# As the central limit theorem predicts, the histogram of the sampling distribution is well approximated by the normal distribution. The outline of the histogram closely follows the normal curve.
# The mean of the sampling distribution, the blue dotted line, overlaps with the population mean, the green solid line. This shows that the two means are essentially equal to each other.
# The sample mean of your first estimate of 50 districts, the red dashed line, is farther away from the center. This is due to sampling variability.

# In[ ]:




