# file=open("data.text",mode="w",encoding="utf-8")  #open file (開啟) utf-8外語輸入法
# file.write("hello\nfile好棒棒")   #write text in the file (寫入或儲存)
# file.close()   #close file (關閉)

#另一種比較好的寫法  a)寫入檔案
# with open("data.text",mode="w",encoding="utf-8") as file:
#     file.write("hello world 好不好")

# #b)讀取檔案
# with open("data.text",mode="r",encoding="utf-8") as file:
#     data=file.read()
# print(data)

# with open("data.text",mode="w") as file:
#     file.write("5\n3\n8\n17\n64")
# sum=0
# with open("data.text",mode="r") as file:
#     for line in file:    #一行一行讀取
#         sum+=int(line)
# print(sum)    #自動加總每行總和

# #使用json格式讀取 寫入資料
# import json
# with open("config.json",mode="r") as file:   #從檔案中讀取json資料放入變數data
#     data=json.load(file)
# print(data)        #data是字典資料
# print("Name:",data["Name"])  #單獨印出來
# print("Age:",data["Age"])

import json
with open("config.json",mode="r") as file:
    data=json.load(file)
print(data)
data["Name"]="Johnson Wu"   #修改資料
with open("config.json",mode="w") as file:  #複寫回檔案中
    json.dump(data,file)
print("Name:",data["Name"])
print("Age:",data["Age"])






