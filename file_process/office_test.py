# -*- coding:utf-8 -*-
'''
使用win32com处理Excel
'''
from Tkinter import Tk
from time import sleep
from tkMessageBox import showwarning
import win32com.client as win32
from urllib2 import urlopen

warn = lambda app:showwarning(app,'Exit?')
RANG = range(3,8)

def excel():
    app = 'Excel'
    x1 = win32.gencache.EnsureDispatch('%s.Application'% app)
    ss = x1.Workbooks.Add()
    sh = ss.ActiveSheet
    x1.Visible = True

    sleep(1)

    sh.Cells(1,1).Value = 'Python-to-%s Demo'%app
    sleep(1)

    url = sinaurl = 'http://hq.sinajs.cn/list=%s'
    stocks = ['sh600000', 'sz000001' ,'sh600004']
    lists = urlopen(url % ','.join(stocks))
    # print('lists==',lists)
    sh.Range(sh.Cells(2,1),sh.Cells(2,2)).Value = ('code_name', 'Yprice')
    sh.Cells(2,3).Value = 'Lprice'
    sh.Range(sh.Cells(2,1),sh.Cells(2,2)).Font.Bold = True
    sh.Cells(2,3).Font.Bold = True
    row = 3
    for data in lists:
        data = data.split('=')
        # print('data==',data)
        data = data[1].split(',')
        # print(data)
        #code,Yprice,Lprice = data.split(',')[0:2]
        code = data[0]
        Yprice = data[1]
        Lprice = data[2]
        #print(data.split(',')[0:2])
        sh.Cells(row,1).Value = code
        sh.Cells(row,2).Value = Yprice
        sh.Cells(row,3).Value = Lprice
        row +=1
        sleep(0.5)

    # for i in RANG:
    #     sh.Cells(i,1).Value = 'Line %d' %i
    #     sleep(1)
    #     print(sh.Cells(i,1).Value)
    # sh.Cells(i+2,1).Value = "Th-th-th-that's all for folks"
    # sh.Range(sh.Cells(4,1),sh.Cells(3,1)).Font.Bold = True

    warn(app)
    ss.Close(False)
    x1.Application.Quit()

def word():
    app = 'Word'
    word = win32.gencache.EnsureDispatch('%s.Application'% app)
    doc = word.Documents.Add()
    word.Visible = True
    sleep(1)

    rng = doc.Range(0,0)
    print('rng=',rng)
    rng.InsertAfter('Python-to-%s Test\r\n\r\n'%app)
    sleep(1)
    for i in RANG:
        rng.InsertAfter('Line %d\r\n'%i)
        sleep(1)
    rng.InsertAfter("\r\nTh-th-th-that's all folks!\r\n")

    warn(app)
    doc.Close(False)
    word.Application.Quit()

def outlook():
    app = 'Outlook'
    olook = win32.gencache.EnsureDispatch('%s.Application' % app)

    mail = olook.CreateItem(win32.constants.olMailItem)
    recip = mail.Recipients.Add('lpb.waln@outlook.com')
    subj = mail.Subject = 'Python-to-%s Demo' % app
    body = ["Line %d " % i for i in RANG]
    body.insert(0, '%s\r\n' % subj)
    body.append("\r\nTh-th-th-that's all folks!")
    mail.Body = "\r\n".join(body)
    mail.Send()

    ns = olook.GetNamespace("MAPI")
    obox = ns.GetDefaultFolder(win32.constants.olFolderOutbox)
    obox.Display()
    obox.Items.Item(1).Display()

    warn(app)
    olook.Quit()

if __name__ == '__main__':
    Tk().withdraw()
    excel()
    # word()
    # outlook()

