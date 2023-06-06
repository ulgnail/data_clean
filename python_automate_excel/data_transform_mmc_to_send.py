#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np

# 读取原始Excel文件的特定表格
df = pd.read_excel('C:\\Users\\Mi\\Desktop\\111.xlsx', sheet_name='1-2 Expense Request Retail')

# 创建一个新的DataFrame，并添加必要的空列
new_df = pd.DataFrame(np.nan, index=range(len(df)), columns=list('ABCDEFGHIJKLMNO'))

# 将原始Excel文件中的特定列拷贝到新的DataFrame中的指定列，并重新命名
new_df.iloc[:, 3] = df.iloc[:, 26]  # Activity Name in D column
new_df.iloc[:, 4] = df.iloc[:, 8]  # Distributor in E column-
new_df.iloc[:, 5] = df.iloc[:, 24]  # Payment Object (KA) in F column
new_df.iloc[:, 7] = df.iloc[:, 19]  # Product in H column
new_df.iloc[:, 8] = df.iloc[:, 9]  # Start Date in I column
new_df.iloc[:, 9] = df.iloc[:, 13]  # End Date in J column
new_df.iloc[:, 10] = pd.to_numeric(df.iloc[:, 20], errors='coerce')  # Unit Incentive in K column
new_df.iloc[:, 11] = pd.to_numeric(df.iloc[:, 21], errors='coerce')  # Forecasted Quantity in L column
new_df.iloc[:, 14] = df.iloc[:, 1]  # Remarks in O column

# 将列名更改为正确的名字
new_df.columns = ['发送状态', 'Country', 'Xiaomi Reference No.', 'Activity Name', 'Distributor', 'Payment Object (KA)', 'Activity Type', 'Product', 'Start Date', 'End Date', 'Unit Incentive', 'Forecasted Quantity', 'Total', 'Currency', 'Remarks']

# 将Country列的前1000行设置为France
new_df.loc[:999, 'Country'] = 'France'

# 计算M列（Total）的值，它应该是K列（Unit Incentive）和L列（Forecasted Quantity）的乘积
new_df['Total'] = new_df['Unit Incentive'] * new_df['Forecasted Quantity']

# 将新的dataframe保存为新的Excel文件
new_df.to_excel('C:\\Users\\Mi\\Desktop\\111_p.xlsx', index=False)




# In[ ]:




