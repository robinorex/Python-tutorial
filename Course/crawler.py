#抓取ptt電影版的網頁原始碼
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
#建立一個request物件 附加Request headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")  #這裡data就是html的原始碼
#print(data)
#解析原始碼 取得每篇文章的標題  pip install beautifulsoup4
import bs4
root=bs4.BeautifulSoup(data, "html.parser")  #html解析工具parser
print(root.title.string)
titles=root.find_all("div",class_="title") #尋找html裡所有class="title"的div標籤
for title in titles:
    if title.a !=None:   #有包含a標籤的話
        print(title.a.string)
with open("data.text3","w",encoding="utf-8") as file:
    for title in titles:
        file.write(title.a.string+"\n")


import urllib.request as req
url="https://www.ptt.cc/bbs/NBA/index.html"
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
print(root.title.string)
titles=root.find_all("div",class_="title")
for title in titles:
    if title.a != None:
        print(title.a.string)

# import urllib.request as req
# url="https://www.quora.com/topic/New-Zealand"
# request=req.Request(url, headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
# })
# with req.urlopen(request) as response:
#     data=response.read().decode("utf-8")
# import bs4
# root=bs4.BeautifulSoup(data, "html.parser")
# print(root.script.string)
# scripts=root.find_all("div",class_="path")
# print(scripts.string)