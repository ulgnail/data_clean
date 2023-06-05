#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[2]:


penguins = sns.load_dataset("penguins")


# In[5]:


penguins.head()


# In[7]:


penguins_sub = penguins[penguins["species"] != "Chinstrap"]
penguins_final = penguins_sub.dropna()
penguins_final.reset_index(inplace = True, drop= True )


# In[8]:


sns.pairplot(penguins_final)


# In[10]:


ols_data = penguins_final[["bill_length_mm", "body_mass_g"]]
ols_formula = "body_mass_g ~ bill_length_mm"
from statsmodels.formula.api import ols


# In[11]:


OLS = ols(formula = ols_formula, data = ols_data)
model = OLS.fit()


# In[12]:


model.summary()


# In[13]:


sns.regplot(x = "bill_length_mm", y = "body_mass_g", data = ols_data)


# In[14]:


# Subset X variable
X = ols_data["bill_length_mm"]

# Get predictions from model
fitted_values = model.predict(X)


# In[15]:


# Calculate residuals
residuals = model.resid


# In[16]:


import matplotlib.pyplot as plt
fig = sns.histplot(residuals)
fig.set_xlabel("Residual Value")
fig.set_title("Histogram of Residuals")
plt.show()


# In[17]:


import matplotlib.pyplot as plt
import statsmodels.api as sm
fig = sm.qqplot(model.resid, line = 's')
plt.show()


# In[18]:


# Import matplotlib
import matplotlib.pyplot as plt
fig = sns.scatterplot(x=fitted_values, y=residuals)

# Add reference line at residuals = 0
fig.axhline(0)

# Set x-axis and y-axis labels
fig.set_xlabel("Fitted Values")
fig.set_ylabel("Residuals")

# Show the plot
plt.show()


# In[ ]:




