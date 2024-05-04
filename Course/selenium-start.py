#載入selenium相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#設定chromedriver執行檔路徑
options=Options()
options.chrome_executable_path="D:\\Python training\\Course\\chromedriver.exe"
#建立driver物件實體，用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://www.google.com/")
driver.save_screenshot("screenshot-google.png")
driver.get("https://www.otago.ac.nz/")
driver.save_screenshot("screehot-otago.png")
driver.close()