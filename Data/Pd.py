import pandas as pd
import numpy as np

rf= pd.read_csv(
    "C:\\Users\\HP\\Downloads\\Documents\\Kiet\\py\\Data\\Code\\A2_Pandas\\P1_Getting_Knowing_Data\\chipotle.tsv",
    sep="\t")

# print(rf.head(5))
# 5 dòng đầu

# dong,cot=rf.shape
# dòng, cột
# print(f'{dong} dòng, {cot} cột')

#rf.info
# 1 số thông tin về dtype non-null column count

# print(rf.index)
#start stop step

# print(rf.describe(include='all'))
# thống kê khá chi tiết

# print(rf.loc[rf.quantity>5])
# tìm cái quantity có giá trị lớn hơn 5

# print(rf.iloc[5:11])
# In từ 5 tới 11

rf.item_price=rf.item_price.apply(lambda x: float(x.replace('$','')))
# Sử dụng lambda với 1 cột nào đó

rf['total_price'] = rf['quantity'] * rf['item_price']


soluongmon=rf.groupby('item_name')['quantity'].sum()
# print(soluongmon.sort_values(ascending=False))
# đúng như cái tên

# rf.item_name.value_counts().count()
# đếm số lượng mỗi món . đếm tổng cộng bao nhiêu món hàng
# bằng với lệnh dưới đây
print(rf.item_name.nunique())