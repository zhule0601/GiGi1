#coding:utf-8
#2.7
#author 朱乐
import os
import urllib
from bs4 import BeautifulSoup
import requests
import time
start = time.clock()

def Spider(url,headers):

    r = requests.get(url,headers=headers)

    soup = BeautifulSoup(r.text,'lxml')

    pattern = soup.find('div',class_='post_entry').find_all('a',class_='caption')

    count = 0

    for urls in pattern:
        for i in range(1,16):
            href = urls['href']
            rull ="http://www.zngirls.com/%s/%d.html"%(href,i)

            html = requests.get(rull,headers=headers)
            soup1 = BeautifulSoup(html.text,'lxml')
            pattern1 = soup1.find('div',class_='photos').find_all('img')

            for  x in pattern1:
                imgurl = x['src']

                print imgurl
                # dir = "F:/GiGi"
                # save_path = dir + "/" + imgurl.replace(':', '1').replace('/', '_')
                #
                # if not os.path.exists(dir):
                #     os.mkdir(dir)
                # urllib.urlretrieve(imgurl,save_path)
        count += 1
        print '第',count,'套'
    print count
if __name__=='__main__':

    urls = 'http://www.zngirls.com/girl/21337/album/'

    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

    Spider(url = urls,headers = headers)
end = time.clock()
print '共用时：',(end-start),'s'
