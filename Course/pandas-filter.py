import pandas as pd
# data=pd.Series([30,15,29])
# condition=data>18
# print(condition)
# print(data[condition])
# data=pd.Series(["hello","paul","piggie"])
# condition=data.str.contains("i")
# print(data[condition])

data=pd.DataFrame({
    "name":["robin","tobin","gasol"],
    "wages":[3000,2000,1000]
})
print(data)
print("===================")
# condition=[False,True,True]
condition=data["wages"]>=1000
print(data[condition])
condition1=data["name"]=="robin"
print(data[condition1])





