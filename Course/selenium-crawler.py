from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options=Options()
options.chrome_executable_path="D:\\Python training\\Course\\chromedriver.exe"
driver=webdriver.Chrome(options=options)
#連線到ptt 
driver.get("https://www.ptt.cc/bbs/Stock/index.html")
# print(driver.page_source)  #連線到網頁原始碼
tags=driver.find_elements(By.CLASS_NAME,"title")  #搜尋屬性是class的所有title標籤(得到列表資料)
for tag in tags:
    print(tag.text)  #取得文章標題
#取得上一頁文章標題
n=0
while n<10:   #抓10頁的標題
    link=driver.find_element(By.LINK_TEXT,"‹ 上頁")
    link.click()  #模擬使用者點擊連結標籤
    tags=driver.find_elements(By.CLASS_NAME,"title")  
    for tag in tags:
        print(tag.text)
    n+=1
driver.close()

