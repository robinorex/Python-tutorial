import pandas as pd
# data=pd.Series([0,20,15,36,40,75,60,128,32,9,17])  #Series 是直向欄位列表(單維度)
# # print(data)
# # print("Max",data.max())
# # print("Median",data.median())
# # print(data*2)
# # print(data==20)  #判斷每個值是不是20 boolean operatorss
# # print(data==0)
# # print(data.size)
# # print(data[0])
# print(data.sum(),data.max(),data.prod(),data.nlargest(4),data.nsmallest(3),data.mean(),data.std())

# data1=pd.DataFrame({
#     "name":["Robin","JOhn","Amy","Candice","Lamar"],
#     "wage":[1200,1245,2450,3550,2323]
# })
# print(data1)
# print(data1["wage"])    #取得特定的欄
# print(data1.iloc[0])   #取得特定的列 iloc[]
# print(data1.dtypes)

#字串
# data=pd.Series(["Pandas","Python","Robin"])
# print(data.str.lower())   #所有字串全部變小寫
# print(data.str.upper())  #所有字串全部變大寫
# print(data.str.len())  #所有字串長度
# print(data.str.cat(sep="-"))
# print(data.str.contains("P"))  #boolean
# print(data.str.replace("Pandas","Hello"))

# #索引
# data=pd.Series([5,4,-2,3,7], index=["a","b","c","d","e"])
# # print(data)
# # print(data.dtype)
# # print(data.size)
# # print(data.index)
# # print(data["e"])
# print(data.sum(),data.max(),data.prod(),data.nlargest(4),data.nsmallest(3),data.mean(),data.std())
# pd.DataFrame({字典},index=[])
data=pd.DataFrame({
    "name":["Robin","Bob","Amy"],
    "wage":[3000,2000,1000]
},index=["a","b","c"])
print(data)
print("================")
# # print("資料數量",data.size)   #有幾個格子
# # print("資料形狀",data.shape)   #(列,欄)
# # print("資料索引",data.index)
# print("取得第三列",data.iloc[2],sep="\n")
# print("取得第b列",data.loc["b"],sep="\n")   #用索引取得列
#取得column直向欄位資料
# print(data["name"],sep="\n")
# print(data["wage"])
# names=data["name"]
# print(names.str.upper())  #全部轉大寫
# wages=data["wage"]
# print(wages.mean())
# print(wages.sum())
# print(wages.nlargest(2))
data["revenue"]=[100000,200000,500000]  #建立新欄位! 
data["rank"]=pd.Series([3,6,1],index=["a","b","c"])
data["cp"]=data["revenue"]/data["wage"]
print(data)
