import pandas as pd
data=pd.read_csv("googleplaystore.csv")  #將csv檔案讀取成dataframe
# print(data)
# print("資料數量",data.shape)
# print("資料欄位",data.columns)
# condition=data["Rating"]<=5    #data cleaning 
# data=data[condition]
# print("平均數",data["Rating"].mean())
# print(data["Rating"].median())
# print(data["Rating"].nlargest(1000).mean())
# print(data["Rating"].nsmallest(100).mean())
#[,+] 這個東西叫做【正則表示式】意思就是把 , 和 + 這兩個符號取代成空白字串，相當於去除的意思
# data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","",regex=True).replace("Free",""))
# print(data["Installs"].mean())
# condition=data["Installs"]>1000000
# print("安裝數量大於1000000的有幾個",data[condition].shape)  #用.shape可以直接得到數量
#關鍵字搜尋
keyword=input("請輸入關鍵字名稱:")
condition=data["App"].str.contains(keyword,case=False)  #大小寫忽略case=False
print(data[condition])
