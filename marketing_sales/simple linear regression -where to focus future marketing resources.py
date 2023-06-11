#!/usr/bin/env python
# coding: utf-8

# In this lab, you are part of an analytics team that provides insights about your company's sales and marketing practices. You have been assigned to a project that focuses on the use of influencer marketing. For this task, you will explore the relationship between your radio promotion budget and your sales.
# 
# The dataset provided includes information about marketing campaigns across TV, radio, and social media, as well as how much revenue in sales was generated from these campaigns. Based on this information, company leaders will make decisions about where to focus future marketing resources. Therefore, it is critical to provide them with a clear understanding of the relationship between types of marketing campaigns and the revenue generated as a result of this investment.

# In[1]:


# Import relevant Python libraries and modules


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols
import statsmodels.api as sm


# In[3]:


# Load the dataset into a DataFrame and save in a variable

file_path = r"C:\Users\Lu LIANG\Desktop\data_clean\data_clean\marketing_sales\marketing_sales_data.csv"

data = pd.read_csv( r"C:\Users\Lu LIANG\Desktop\data_clean\data_clean\marketing_sales\marketing_sales_data.csv")


# In[6]:


# Display the first 10 rows of the data
data.head(10)


# The data includes the following information:
# TV promotion budget (expressed as "Low", "Medium", or "High")
# Radio promotion budget
# Social media promotion budget
# Type of influencer that the promotion is in collaboration with (expressed as "Mega", "Macro", or "Micro", or "Nano")
# Note: Mega-influencers have over 1 million followers, macro-influencers have 100,000 to 1 million followers, micro-influencers have 10,000 to 100,000 followers, and nano-influencers have fewer than 10,000 followers.
# Sales accrued from the promotion

# In[7]:


# Display number of rows, number of columns

data.shape


# There are 572 rows and 5 columns in the data. One way to interpret this is that 572 companies are represented in the data, along with 5 aspects about each company that reveals how they promote their products/services and the sales accrued from their promotion.
# 

# In[8]:


# Step 1. Start with .isna() to get booleans indicating whether each value in the data is missing

data.isna()


# In[9]:


data.isna().any(axis=1)


# In[10]:


data.isna().any(axis=1).sum()


# There are 3 rows containing missing values, which is not that many, considering the total number of rows. It would be appropriate to drop these rows that contain missing values to proceed with preparing the data for modeling.

# In[11]:


data = data.dropna(axis=0)


# In[12]:


data.isna().any(axis=1).sum()


# In[13]:


# Create plot of pairwise relationships

sns.pairplot(data)


# In the scatter plot of Sales over Radio, the points appear to cluster around a line that indicates a positive association between the two variables. Since the points cluster around a line, it seems the assumption of linearity is met.

# In[14]:


ols_data = data[["Radio", "Sales"]]


# In[15]:


ols_data.head(10)


# In[16]:


ols_formula = "Sales ~ Radio"


# In[17]:


OLS = ols(formula = ols_formula, data = ols_data)


# In[18]:


# Fit the model to the data
# Save the fitted model in a variable

model = OLS.fit()


# In[19]:


model.summary()


# If a company has a budget of 1 million dollars more for promoting their products/services on the radio, the company's sales would increase by 8.1733 million dollars on average.
# Another interpretation: Companies with 1 million dollars more in their radio promotion budget accrue 8.1733 million dollars more in sales on average.

# In[20]:


sns.regplot(x = "Radio", y = "Sales", data = ols_data)


# The preceding regression plot illustrates an approximately linear relationship between the two variables along with the best fit line. This confirms the assumption of linearity.

# Check the normality assumption.

# In[21]:


# Get the residuals from the model

residuals = model.resid


# In[22]:


# Visualize the distribution of the residuals

fig = sns.histplot(residuals)
fig.set_xlabel("Residual Value")
fig.set_title("Histogram of Residuals")
plt.show()


# Based on the preceding visualization, the distribution of the residuals is approximately normal. This indicates that the assumption of normality is likely met.

# Create a Q-Q plot to confirm the assumption of normality

# In[24]:


# Create a Q-Q plot 

sm.qqplot(residuals, line='s')
plt.title("Q-Q plot of Residuals")
plt.show()


# In the preceding Q-Q plot, the points closely follow a straight diagonal line trending upward. This confirms that the normality assumption is met.

# Check the assumptions of independent observation and homoscedasticity

# In[26]:


# Get fitted values

fitted_values = model.predict(ols_data["Radio"])


# In[27]:


# Create a scatterplot of residuals against fitted values

fig = sns.scatterplot(x=fitted_values, y=residuals)
fig.axhline(0)
fig.set_xlabel("Fitted Values")
fig.set_ylabel("Residuals")
plt.show()


# In the preceding scatterplot, the data points have a cloud-like resemblance and do not follow an explicit pattern. So it appears that the independent observation assumption has not been violated. Given that the residuals appear to be randomly spaced, the homoscedasticity assumption seems to be met.

# ## Conclusion

# **What are the key takeaways from this lab?**
# - Data visualizations and exploratory data analysis can be used to check if linear regression is a well suited approach for modeling the relationship between two variables.
# - The results of a linear regression model can be used to express the relationship between two variables. 
# 
# **What results can be presented from this lab?**
# 
# In the simple linear regression model, the y-intercept is 41.5326 and the slope is 8.1733. 
#     One interpretation: If a company has a budget of 1 million dollars more for promoting their products/services on the radio, the company's sales would increase by 8.1733 million dollars on average.
#     Another interpretation: Companies with 1 million dollars more in their radio promotion budget accrue 8.1733 million dollars more in sales on average.
# 
# 
# The results are statistically significant with a p-value of 0.000, which is a very small value (and smaller than the common significance level of 0.05). This indicates that there is a very low probability of observing data as extreme or more extreme than this dataset when the null hypothesis is true. In this context, the null hypothesis is that there is no relationship between radio promotion budget and sales i.e. the slope is zero, and the alternative hypothesis is that there is a relationship between radio promotion budget and sales i.e. the slope is not zero. So, you could reject the null hypothesis and state that there is a relationship between radio promotion budget and sales for companies in this data.
# 
# The slope of the line of best fit that resulted from the regression model is approximate and subject to uncertainty (not the exact value). The 95% confidence interval for the slope is from 7.791 to 8.555. This indicates that there is a 95% probability that the interval [7.791, 8.555] contains the true value for the slope. 
# 
# **How would you frame your findings to external stakeholders?**
# 
# Based on the dataset at hand and the regression analysis conducted here, there is a notable relationship between radio promotion budget and sales for companies in this data, with a p-value of 0.000 and standard error of 0.194. For companies represented by this data, a 1 million dollar increase in radio promotion budget could be accociated with a 8.1733 million dollar increase in sales. It would be worth continuing to promote products/services on the radio. Also, it is recommended to consider further examining the relationship between the two variables (radio promotion budget and sales) in different contexts. For example, it would help to gather more data to understand whether this relationship is different in certain industries or when promoting certain types of products/services. 

# References
# 
# Pandas.DataFrame.Any — Pandas 1.4.3 Documentation. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.any.html.
# 
# Pandas.DataFrame.Isna — Pandas 1.4.3 Documentation. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html.
# 
# Pandas.Series.Sum — Pandas 1.4.3 Documentation. https://pandas.pydata.org/docs/reference/api/pandas.Series.sum.html.
# 
# Saragih, H.S. Dummy Marketing and Sales Data. https://www.kaggle.com/datasets/harrimansaragih/dummy-advertising-and-sales-data.

# In[ ]:




