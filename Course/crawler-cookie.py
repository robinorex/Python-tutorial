import urllib.request as req
def getdata(url):    #用函式做包裝
    request=req.Request(url, headers={
        'cookie':'over18=1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div", class_="title")
    for title in titles:
        if title.a != None:
            print(title.a.string)
    nextlink=root.find("a",string="‹ 上頁") #找到內文是‹ 上頁的a標籤 抓取上一頁的連結
    return nextlink["href"]
#主程序: 抓取多個頁面的標題!!!
Pageurl="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3:
    Pageurl="http://www.ptt.cc"+getdata(Pageurl)
    count+=1

# import json
# data=data.replac("])}while(1);</x>","")
# data=json.loads(data)            #把原始json資料解析成字典列表的表示形式
# posts=data["payload"]["references"]["Post"]
# for key in posts:
#     post=posts[key]
#     print(post["title"])

