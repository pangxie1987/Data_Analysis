# -*- coding:utf-8 -*-
'''
使用csv库进行csv文件处理
'''
import csv
import os
import sys
from collections import namedtuple

os.path.sys
sys.path.append('.')

# files=os.listdir()
# for file in files:
#     #print(file)

def readcsvdata():
    # 使用csv.reader读取csv中的数据
    with open('DrawLines\datas\dl_done.csv') as f:
        datas=csv.reader(f)
        for data in datas:
            print(data)
def readcsvrowdata():
    
    #根据指定的列名，输出这一列的数据
    with open ('DrawLines\datas\dl_done.csv') as f:
        f_csv=csv.reader(f)
        headings=next(f_csv)
        Row=namedtuple('Row',headings)
        for r in f_csv:
            row=Row(*r)
            #根据指定列名输出数据
            print(row.SEATID_)
def readcsvdictdata():
    # 将数据读取到字典中进行访问
    with open ('DrawLines\datas\dl_done.csv') as f:
        # 构造字典
        f_csv=csv.DictReader(f)
        for row in f_csv:
            # 输出SEATID_
            print(row['SEATID_'])

def write2csv():
    # 数据写入csv文件中
    headers = ['Symbol','Price','Date','Time','Change','Volume']
    rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
            ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
            ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
        ]

    # newline=''去除windows系统自动加的空行
    with open ('DrawLines\datas\stocks.csv','w',newline='') as f:
        f_csv=csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)
        print('Write Sucess ！')

write2csv()