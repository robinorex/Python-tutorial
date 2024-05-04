from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options=Options()
options.chrome_executable_path="D:\\Python training\\Course\\chromedriver.exe"
driver=webdriver.Chrome(options=options) 
driver.get("https://www2.nchu.edu.tw/news/id/1")
# n=0
# while n<3:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
#     n+=1
n=0
while n<5:
    link=driver.find_element(By.CLASS_NAME,"next")
    link.click()
    titleTags=driver.find_elements(By.CLASS_NAME, "title")
    for titleTag in titleTags:
        print(titleTag.text)
    n+=1
driver.close()

