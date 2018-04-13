# -*- coding=utf-8 -*-
'''
使用tushare库获取行情数据
http://tushare.waditu.com/
https://www.cnblogs.com/DreamRJF/p/8660630.html
安装列表
tushare

'''

import pandas as pd
import tushare as ts
import time
import matplotlib.pyplot as plt
import numpy as np


start='2018-01-01'
end=time.strftime('%Y-%m-%d')

print(end)


# 获取历史行情数据

# data_hist=ts.get_hist_data('600004',start,end)
# data_hist.to_csv('.\datas\600004_hist.csv')
#
# print(data_hist)


'''
该函数只返回开盘价（open）、最高价（high）、收盘价（close）、
最低价（low）、成交量（volume）、成交金额（amount）六列 
'''
# data_h=ts.get_h_data('600004',start,end)
# data_h.to_csv('.\datas\600004_h.cav')
# print(data_h)


# 获取实时行情数据

# data_today=ts.get_today_ticks(code='600000', retry_count=3, pause=0.01)
# print(data_today)

'''
获取电影票房数据
month_boxoffice
'''

# 获取上一个月的电影票房
# data_movie=ts.month_boxoffice()
# data_movie.to_csv('.\datas\movie.csv')

# ---------------绘制线状图---------------
data_movie_r=pd.read_csv('.\datas\movie.csv')
print(data_movie_r)
data_movie_r['box_pro'].plot(legend=True, figsize=(10,4))
#plt.show()

# ---------------绘制饼图---------------

# step1 获取需要的数据
# 获取第三列的数据，电影名称、票房纪录，并分别构造列表
names=pd.read_csv('.\datas\movie.csv')['MovieName']
WomIndexs=pd.read_csv('.\datas\movie.csv')['WomIndex']
name=[]
WomIndex=[]

n=0
for i in names:
    if int(n)<10:
        name.append(i)
    n+=1

print(name)

m=0
for j in WomIndexs :
    if int(m)<10:
        WomIndex.append(j)
    m+=1
print(WomIndex)

# step2 设置颜色
color=['#9999ff', '#ff9999', '#7777aa', '#2442aa', '#dd5555',
       '#9988ff','#9977ff','#9944ff','#2442ff','#2882aa']

# step3 处理中文乱码和坐标轴负号问题
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
#
# # step4 将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则为椭圆
# plt.axes(aspect='equal')
#
# # step5 控制x轴和y轴的范围
# plt.xlim( 0, 4)
# plt.ylim( 0, 4)
#
# # step6 绘图
# plt.pie(x=WomIndex,labels=name,colors=color)
#
# # step7 删除x轴和y轴的刻度
# plt.xticks(())
# plt.yticks(())
#
# # step8 添加图标题
# plt.title('上月电影票房分布')
#
# # 保存图片
# plt.savefig(u'电影票房饼图')
# #plt.show()

# ---------------绘制柱状图---------------
# https://jingyan.baidu.com/article/4f7d5712af077e1a21192773.html

# 创建一个DataFrame np.random.rand(10,4),
df=pd.DataFrame( np.random.rand(1,10) , columns=name)
print(df.head())

# 设置样式(最大行数、列数)
pd.set_option('display.max_rows',5)
pd.set_option('display.max_columns',5)


# 绘图
pt=df.plot(kind='bar').get_figure()

#pt.show()

#--------------频率直方图--------------
# https://blog.csdn.net/qq_22238533/article/details/71598330

pd.Series.value_counts(data_movie_r['days']).plot.bar()

plt.show()