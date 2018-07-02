#-*-coding: utf-8-*-
'''
get quotes from yahoo
'''

# ticks = ('YHOO', 'GOOG', 'EBAY', 'AMZN')
# URL = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=sl1c1p2' # f=sl1c1p2中的s、l1、c1和p2分别代表股票订单号、上次交易价格、变化量和变化率

# print '\nPrice quoted as of:', ctime()
# print '\nTICKER'.ljust(9), 'PRICE'.ljust(8), 'GHG'.ljust(5), '%AGE'
# print '------'.ljust(8), '-----'.ljust(8), '---'.ljust(5), '----'
# u = urlopen(URL % ','.join(ticks))

# for row in u:
#     tick, price, chg, per = row.split(',')
#     print eval(tick).ljust(7), ('%.2f' % round(float(price), 2)).rjust(6), chg.rjust(6), eval(per.rstrip()).rjust(6)
# u.close()

'''
get quotes data from sina
'''
from colorama import init,Fore,Back,Style
from time import ctime
from urllib2 import urlopen
import time
import sqlite3
import chardet

# stocks = ['sh600000','sh600004','sz300104','sh600006']
# sinaurl='http://hq.sinajs.cn/list=%s'
# print('code_name'+'\t'+'L_Price'+'\t'+'Update_time')
# # word = raw_input('input Q to exit!')
# while 1:
#     # if word = 'Q':
#     #     break
#     url = sinaurl % ','.join(stocks)
#     # print(url)
#     data = urlopen(sinaurl % ','.join(stocks))
#     for i in data:
#         i = i.split('=')
#         i = i[1].split(',')
#         # print(i[0].split('\"'))[1]
#         print('%-16s%-10s%-10s')%(i[0].split('\"')[1],i[3],i[-2])
#         # print(i[0],i[3],i[-2])
#         time.sleep(0.5)


conn = sqlite3.connect('sinaquotes')
cur = conn.cursor()

sql_crete = 'create table sina_quotes(STKNAME VARCHAR(35),STKCODE VARCHAR(35),ZRCJ NUMBER(18,4), ZJCJ NUMBER(18,4))'
sql_select = 'select * from sina_quotes'

def insert(sql):
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)

insert(sql_crete)

def select(sql):
    try:
        data = cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
    else:
        print(data.fetchall())

# select(sql_select)

# rows = cur.execute('select STKNAME,STKCODE,ZRCJ,ZJCJ from sina_quotes ')
# for row in rows:
#     print(row[0])


def get_quote():
    '''
    获取行情列表数据
    '''
    sinaurl = 'http://hq.sinajs.cn/list=%s'
    stocks = raw_input('Enter your code!>\n')
    stocks = stocks.split(',')
    init(autoreset=True)
    print('code_name'+'\t'+'L_Price'+'\t'+'Update_time')
    while 1:
        n = 0
        data = urlopen(sinaurl % ','.join(stocks))
        for i in data:
            i = i.split('=')
            i = i[1].split(',')
            stkname = (i[0].split('\"'))[1]

            ZRSP = i[2]  #获取昨日收盘价
            ZJCJ = i[3]  #获取最近成交价
            if ZJCJ > ZRSP: #根据最新价和昨收价的关系，确定终端的颜色
                print(Fore.RED+'%-16s%-10s%-10s')%(i[0].split('\"')[1],i[3],i[-2])
            elif ZJCJ < ZRSP:
                print(Fore.GREEN+'%-16s%-10s%-10s')%(i[0].split('\"')[1],i[3],i[-2])
            else:
                print('%-16s%-10s%-10s')%(i[0].split('\"')[1],i[3],i[-2])
            # insert to sqlite3
            # mycode = str(stocks[n])
            # print(mycode)
            # print(type(mycode))
            sql_insert = "insert into sina_quotes (STKNAME,STKCODE,ZRCJ,ZJCJ) values("'"+%s+"'", "'"+%s+"'",%s,%s )"%(stocks[n], stocks[n], ZRSP, ZJCJ)
            # print(sql_insert)
            insert(sql_insert)

        time.sleep(0.5)
        print('='*50)

# get_quote()

#执行方式  python sinaquotes.py sh600000,sz000001

'''
Test colormara  terminal color set for windows and linux
https://blog.csdn.net/gatieme/article/details/45439671
'''
