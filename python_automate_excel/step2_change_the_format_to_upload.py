#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

# 读取Excel文件
df = pd.read_excel(r'C:\Users\Mi\Desktop\sys_to_clean_w20_f_w19_prossed.xlsx', engine='openpyxl')

# 将第一列重命名为 Product_ID，使其在 melt 操作中更清晰
df.rename(columns={df.columns[0]: 'Product_ID'}, inplace=True)

# 使用 pandas 的 melt 方法将数据从宽格式转换为长格式
# 其中，id_vars 参数设置不需要被转换的列，var_name 参数设置新的列名，value_name 设置新的值的列名
df_melted = df.melt(id_vars='Product_ID', var_name='Store', value_name='Sales')

# 保存新的DataFrame为Excel文件
df_melted.to_excel(r'C:\Users\Mi\Desktop\sys_to_clean_w20_f_w19_prossed_handon.xlsx', index=False, engine='openpyxl')






# In[ ]:





# In[ ]:




