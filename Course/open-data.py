import urllib.request as request  #連接網路上的資料
with request.urlopen("http://www.ntu.edu.tw/") as response:
    data=response.read().decode("utf-8")
print(data)   #得到原始碼(HTML, CSS, JS)

# import urllib.request as request
# with request.urlopen() as response:
#     data=response.read()
# print(data)

import urllib.request as request
import json
with request.urlopen("https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire") as response:
    data=json.load(response)    #利用json模組處理json資料格式
comlist=data["result"]["results"]
with open("data.text","w",encoding="utf-8") as file:
    for company in comlist:
        file.write(company["公司名稱"]+"\n")

import urllib.request as request
import json
with request.urlopen("https://data.taipei/api/v1/dataset/74cfc01d-242f-428d-bc2f-caf5edd6e404?scope=resourceAquire") as response:
    data=json.load(response)
parklist=data["result"]["results"]
with open("data.text1","w",encoding="utf-8") as file:
    for park in parklist:
        file.write(park["停車場名稱"]+"\n")

import urllib.request as request
import json
with request.urlopen("https://data.taipei/api/v1/dataset/6d38ddf5-ae05-4dab-ac24-1e05f5841b01?scope=resourceAquire") as response:
    data=json.load(response)
bikelist=data["result"]["results"]
with open("data.text2","w") as file:
    for bike in bikelist:
        file.write(bike["longitude2"]+"\n")
