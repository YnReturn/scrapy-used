from concurrent import futures
import requests
import os,time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# startLink，第一级跳转
startLink = ['http://moe.005.tv/moeimg/tb/', 'http://moe.005.tv/moeimg/bz/', 'http://moe.005.tv/moeimg/sjbz/', 'http://moe.005.tv/cosplay/']
#图片链接
imgSrc = []
pageLink = []

# 依次获取startLinK列表中的所有img页面的链接; 补充添加到imgLink列表；
def req(url):
    headers = {'User-Agent': UserAgent().random}
    html = requests.get(url, headers = headers)
    soup = BeautifulSoup(html.text, 'lxml')
    return soup 

# 图片保存
def save(isrc, i):
    response = requests.get(url=isrc, headers={'User-Agent': UserAgent().random})
    pic = response.content
    if isrc[-3:] == 'png':
        print('正在请求--->')
        with open('E:/pic/%d.png' % i, 'wb') as f:
            f.write(pic)
        print('获取请求---> %d successful!'% i)
    if isrc[-3:] == 'jpg':
        print('正在请求--->')
        with open('E:/pic/%d.jpg' % i,'wb') as f:
            f.write(pic)
        print('获取请求---> %d successful!' % i)       
		 
# 依次获取img页面的src的链接;
def getPage_link(url):
    global pageLink
    soup = req(url)
    # 当前页面中的 li 所在容器的位置
    page = soup.find('div',{'class':'zhuti_w_list'})
    div_a = page.findAll('a')
    for i in div_a:
        pageLink.append(i.get('href'))
    print('page li->href')
    # 获取页脚所有的“下一页”
    page = soup.find('div',{'class':'dede_pages'})
    div_a = page.findAll('a')
    for i in range(1,len(div_a)):
        htmlSoup = req(url+div_a[i].get('href'))
        # 直接循环求取所有“下一页”中的 li 容器链接
        htmlPage = htmlSoup.find('div',{'class':'zhuti_w_list'})
        div_b = htmlPage.findAll('a')
        for i in div_b:
            pageLink.append(i.get('href'))
    print('get number!')
    return 0

def getImg_src():
    global imgSrc
    for _ in pageLink:
        print('for _ in pageLink:')
        soup = req(_)
        imgItem = soup.find('div',{'class':'content_nr'})
        img = imgItem.findAll('img')
        for i in img:
            imgSrc.append(i.get('src'))
    return 1

def main():
    for i in startLink:
        getPage_link(i)
    getImg_src()
    for i in range(1,len(imgSrc)):
        save(imgSrc[i],i)


if __name__ == '__main__':
    print('starting!')
    main()
    print('worked!')

