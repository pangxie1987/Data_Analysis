# -*- coding=utf-8 -*-
'''

利用pandas_datareader直接从互联网获取行情数据，并将数据可视化
https://blog.csdn.net/robertsong2004/article/details/52233176

安装列表
pandas_datareader
matplotlib
'''

import pandas_datareader.data as web
#import pandas.io.data as web
import datetime
import matplotlib.pyplot as plt


start=datetime.datetime(2017,1,1)
end=datetime.date.today()

'''
从互联网读取单个数据（yahoo来源）
获取Yahoo数据必须使用以下插件 https://pypi.python.org/pypi/fix-yahoo-finance
报错解决办法 https://blog.csdn.net/panfengzjz/article/details/79721235
'''

# import fix_yahoo_finance as yf
# yf.pdr_override()
# apple=web.get_data_yahoo('AAPL',start,end)
# print(apple.head())



# 从互联网读取多个数据（其他来源）
apple=web.DataReader('AAPL.US','quandl',start,end)
print(apple.head(n=3))


# # 数据写入到csv文件
# apple.to_csv('.\datas\apple.csv')


# 数据可视化
apple['Adj Close'].plot(legend=True, figsize=(10,4))
plt.show()
