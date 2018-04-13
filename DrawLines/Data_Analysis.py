# -*- coding=utf-8 -*-
'''
读取数据，并展示数据格式
'''
import pandas as pd
import matplotlib.pyplot as plt

filename=".\datas\dl_done.csv"

print(filename)
data=pd.read_csv(filename)
# print(data.columns)
# print('+'*50)
# print(data.index)
#
# print(data.T)

data.plot(kind='box')
# print('plot',data.plot(kind='box'))

plt.show(kind='box')
