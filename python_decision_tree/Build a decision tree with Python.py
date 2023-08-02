#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# This function displays the splits of the tree
from sklearn.tree import plot_tree

from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
from sklearn.metrics import recall_score, precision_score, f1_score, accuracy_score


# In[9]:


# Read in data
file = 'Churn_Modelling.csv'
csv_file_path = 'C:\\Users\\Lu LIANG\\Desktop\\Churn_Modelling.csv'
df_original= pd.read_csv('C:\\Users\\Lu LIANG\\Desktop\\Churn_Modelling.csv')
df_original.head()


# In[10]:


# Check class balance
df_original['Exited'].value_counts()


# In[11]:


# Calculate average balance of customers who churned
avg_churned_bal = df_original[df_original['Exited']==1]['Balance'].mean()
avg_churned_bal


# # Feature engineering

# In[12]:


# Create a new df that drops RowNumber, CustomerId, Surname, and Gender cols
churn_df = df_original.drop(['RowNumber', 'CustomerId', 'Surname', 'Gender'], 
                            axis=1)


# In[13]:


churn_df.head()


# In[14]:


# Dummy encode categorical variables
churn_df = pd.get_dummies(churn_df, drop_first=True)


# In[15]:


churn_df.head()


# ## Split the data

# In[17]:


# Define the y (target) variable
y = churn_df['Exited']

# Define the X (predictor) variables
X = churn_df.copy()
X = X.drop('Exited', axis=1)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.25, stratify=y, 
                                                    random_state=42)


# # Baseline model

# In[18]:


# Instantiate the model
decision_tree = DecisionTreeClassifier(random_state=0)

# Fit the model to training data
decision_tree.fit(X_train, y_train)

# Make predictions on test data
dt_pred = decision_tree.predict(X_test)


# In[19]:


# Generate performance metrics
print("Accuracy:", "%.3f" % accuracy_score(y_test, dt_pred))
print("Precision:", "%.3f" % precision_score(y_test, dt_pred))
print("Recall:", "%.3f" % recall_score(y_test, dt_pred))
print("F1 Score:", "%.3f" % f1_score(y_test, dt_pred))


# A comparison of F1 scores reveals that the decision tree is an improvement to the Naive Bayes model we built earlier. For reference, here are the scores of both models:
# 
# | Model | F1 | Recall | Precision | Accuracy |
# | :- | :-: | :-: | :-: | :-: |
# | Decision Tree | 0.494 | 0.503 | 0.486 | 0.790 |
# | Naive Bayes | 0.456 | 0.369 | 0.597 | 0.821 |
# 

# # Analysis of baseline model

# In[20]:


def conf_matrix_plot(model, x_data, y_data):
    '''
    Accepts as argument model object, X data (test or validate), and y data (test or validate). 
    Returns a plot of confusion matrix for predictions on y data.
    ''' 
  
    model_pred = model.predict(x_data)
    cm = confusion_matrix(y_data, model_pred, labels=model.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                             display_labels=model.classes_)
  
    disp.plot(values_format='')  # `values_format=''` suppresses scientific notation
    plt.show()


# In[21]:


# Generate confusion matrix
conf_matrix_plot(decision_tree, X_test, y_test)


# In[22]:


# Plot the tree
plt.figure(figsize=(15,12))
plot_tree(decision_tree, max_depth=2, fontsize=14, feature_names=X.columns, 
          class_names={0:'stayed', 1:'churned'}, filled=True);
plt.show()


#  This plot tells us that, if we could only do a single split on a single variable, the one that would most help us predict whether a customer will churn is their age.
# 
# If we look at the nodes at depth one, we notice that the number of products and whether or not the customer is an active member also are both strong predictors (relative to the features we have) of whether or not they will churn. 
# 
# This is a good indication that it might be worthwhile to return to your EDA and examine these features more closely. 
# 
# Finally, it's worth noting that there is no single question that can be asked&mdash;for any feature&mdash;that would cause a majority of samples in one of the child nodes to be of class "churned." The tree must get to depth two (i.e., two questions must be asked) before this happens.
