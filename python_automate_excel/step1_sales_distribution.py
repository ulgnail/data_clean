#!/usr/bin/env python
# coding: utf-8

# ##表格格式
#    A1     B1  C1         D1
# 1  ID     SO  MIFRD02690 MIFRD00910
# 1 41319 461
# 1 41319 367
# 

# In[9]:


import pandas as pd

# 读取Excel文件
df = pd.read_excel(r'C:\Users\Mi\Desktop\sys_to_clean_w20_f_w19.xlsx', engine='openpyxl')

# 获取商店的数量
num_shops = len(df.columns) - 2  # 第一列是ID，第二列是产品销量，其他列都是商店

# 遍历每一行
for index, row in df.iterrows():
    # 获取产品销量
    product_quantity = row['SO']

    # 分配产品到每个商店
    for i in range(2, 2 + num_shops):
        # 检查当前商店的销售总额是否已经达到15，如果已经达到15，跳过当前商店
        if df.iloc[:, i].sum() >= 15:
            continue
        # 如果产品数量足够，每个商店至少分配一个产品
        elif product_quantity > 0:
            df.iloc[index, i] = 1
            product_quantity -= 1
        # 如果产品数量不足，结束分配
        else:
            break

# 分配剩余的产品到其他的商店
for index, row in df.iterrows():
    product_quantity = row['SO'] - df.iloc[index, 2:].sum()
    if product_quantity > 0:
        for i in range(2, 2 + num_shops):
            # 检查当前商店的销售总额是否已经达到15，如果已经达到15，跳过当前商店
            if df.iloc[:, i].sum() >= 15:
                continue
            elif product_quantity > 0:
                df.iloc[index, i] += 1
                product_quantity -= 1
            else:
                break

# 将空白单元格填充为0
df.fillna(0, inplace=True)

# 保存处理后的Excel文件
df.to_excel(r'C:\Users\Mi\Desktop\sys_to_clean_w20_f_w19_prossed.xlsx', index=False, engine='openpyxl')


# In[ ]:




