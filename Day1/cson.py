from urllib import request
def fun(blocknum,blocksize,totalsize):
    """
    blocknum:当前的块编号
    blocksize:每次传输的块大小
    totalsize:网页文件总大小
    """
    percent = blocknum*blocksize/totalsize
    if percent > 1.0:
        percent = 1.0
    percent = percent*100
    print("download : %.2f%%" %(percent))
url = "http://www.baidu.com"
path = r"C:\Users\Administrator\Desktop\download\sina.html"
request.urlretrieve(url, path, fun)
