#比較一下範例檔案中的「File I/O」與「CSV Reader」讀出來的內容有什麼差異
import csv
with open ('example.csv' ,encoding = 'utf8') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=',')
    for row in readcsv:
        #print(row)

        readfio = open ('example.csv' ,'r')
        #print(readfio)
#csv reader會讀取檔案內部的資料
#File I/O 會告訴我們檔案的屬性如下所示
#<_io.TextIOWrapper name='example.csv' mode='r' encoding='cp950'>


#根據範例檔案的結果：

#1. 取出班次一的每一個時間，印出來就好
#2. 將班次一的每一個時間用一個變數保存
#3. 將所有班次和其每一個時間用一個變數保存
#(Hint： 2&3 要想一下用什麼的資料型態做整理比較適合)


#1. 取出班次一的每一個時間，印出來就好
import csv
#  open的encoding會因平台不同而不同=>這裡他是讀不出來中文才出現
# nicodeDecodeError: 'cp950' codec can't decode byte
with open('example.csv' ,encoding = 'utf8') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=',')
    times_one = []
    all_times = []

#readcsv是全部的資料
    for row in readcsv:  
#2. 將班次一的每一個時間用一個變數保存
        times_one = row[5]
#3. 將所有班次和其每一個時間用一個變數保存
        all_times = [row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15]]
        #還在測試中
        #import unmpy as times
        #atimes = times.array([row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15]])
        #print (atimes)