set1={3,4,5,6,7,444,123123}
print(1 in set1)
print(3 in set1)
print(10 not in set1)
set2={4,5,6,9}
s3=set1&set2  #&交集
print(s3)
s4=set1|set2  #|聯集
print(s4)
s5=set1-set2 #-差集
print(s5)
s6=set2-set1
print(s6)
s7=set1^set2  #^反交集
print(s7)
s=set("hello")  #set字串 沒順序性
print(s)
print("h" in s)
print("s"in s)
k=set("whatare you doing")
print(k)
dic={"apple":"貧果", "bug":"重重"}  #字典 key:value配對
print(dic["apple"])
print("apple"in dic)
del dic['apple']
print(dic)
dic={x:x**4 for x in [1,2,3,4,5,6,7]}  #4次方的意思
print(dic)