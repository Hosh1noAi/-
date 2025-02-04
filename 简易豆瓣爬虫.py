import requests
from bs4 import BeautifulSoup

headers={
    
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36" #伪装成网页，绕过反爬虫
    
}
for num in range(0,250,25):
    response=requests.get(f"https://movie.douban.com/top250?start={num}",headers=headers)   #循环查询从第一个到底250个，25个一页，否则不需要？start=。。。
    html = response.text
    soup = BeautifulSoup(html,"html.parser")
    all_titles = soup.findAll("span",attrs={"class":"title"})   #具体以每个网页自身的构造进行调整，不一定是span，title啥的
    for title in all_titles:
        title_string=title.string
        if "/" not in title_string:   #去除/，保留纯净中文标题
            print(title_string)
    



   
   
      