#Iterable資料型態: list, dic, set, string
#for 變數名稱 in Iterable:
# for x in [3,5,2]:
#     print(x)
# for x in "abc":
#     print(x)
# for x in {"a","test",3,5}:     #set列印出來沒有順序性
#     print(x)
# for key in {"a":7,"b":8}:   #字典迴圈只針對key跑值
#     print(key)               
# dic={"a":7,"b":8}
# for key in dic:
#     print(dic[key])        #print 出value
#內建函式
#max(可跌代資料)
result=max([3,5,2,1])
print(result)
result=max("robin")   #選字母順序在最後面的
print(result)   
result=max({"A":"apple","B":"book"})     #在AB之間選資母順序後面的!!!
print(result)
#sorted(可跌代資料)
result=sorted("wwteragerrgpijsdfphiertpeiorjgpaerogjp") #sorted按照字母順序排序
print(result)
result=sorted({-5,10,20,15,172,66})
print(result)