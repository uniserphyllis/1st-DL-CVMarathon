#1.（簡答題）檔案、API、爬蟲三種取得資料方式有什麼不同？
    #檔案和API是開發者主動提供的，其中檔案是包好的資料，要下載才能做使用，而API是直接提供開發者連接資料的接口，爬蟲則是沒有提供以上兩種資料時直接解析頁面上資料。

#2.（實作）完成一個程式，需滿足下列需求：
    #「下載指定檔案到 Data 資料夾，存成檔名 Homework.txt」的檔案網址
    #檢查 Data 資料夾是否有 Homework.txt 檔名之檔案
    #將「Hello World」字串覆寫到 Homework.txt 檔案
    #檢查 Homework.txt 檔案字數是否符合 Hello World 字數b


#「下載指定檔案到 Data 資料夾，存成檔名 Homework.txt」的檔案網址
# *可惡:Python3 之後的urllib都要加request才能運作
import os
import urllib.request
os.makedirs('./Data/',exist_ok = True)
urlfile = urllib.request.urlretrieve('https://www.w3.org/TR/PNG/iso_8859-1.txt','./Data/Homework.txt')
  
#檢查 Data 資料夾是否有 Homework.txt 檔名之檔案
if os.path.isfile('./Data/Homework.txt'):
  print("檔案存在。")
else:
  print("檔案不存在。")

#將「Hello World」字串覆寫到 Homework.txt 檔案

refile = open('Homework.txt','w')
refile.write('Hello Word')
refile.close()

#檢查 Homework.txt 檔案字數是否符合 Hello World 字數b

checkfile = open('Homework.txt','r')
for hw in checkfile:
    outhw = hw

print (len(outhw) == len('Hello Word'))
