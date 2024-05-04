grades=[12,24,33,95]
print(grades[0])
grades[0]=55
grades[1:3]=[]
grades=grades+[1,2]
grades 
length=len(grades)
print(length)
data=[[3,4,5],[6,7,8]]
data[0][1]
data[0][1]=[5,5]
print(data)
data[0][0:2]=[5,5,5] 
grades=[12,60,15,70,90]
print(grades)
print(grades[0])
print(grades[1:5])
grades[1:4]=[]
print(grades)
grades1=grades+[1,2]  #列表串接 不是加上去
print(grades1)
print(len(grades1)) #lenght 
data=[[2,3,4],[5,7,9]]  #巢狀列表
print(data[0][2])   #第一層 第二個數 (python都是0開始)
print(data[1][1]) 
data[1][0:2]=[5,5,5]
print(data)   #list用中括號有序可變動列表  tuple用小括號有序不可變動列表
data=(3,3,5)
data[0]=5
#中括號就是列表!!!!