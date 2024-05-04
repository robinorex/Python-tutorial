# import random  #隨機選取
# data=random.choice([0,3,2,5,4,3,2,1])
# data=random.sample([3,4,1,2,4,5,7,0,12,123123,443],4) #隨機選4筆
# print(data)
# import random
# # data=[3,5,8,20]
# # random.shuffle(data)
# # print(data)
# data=random.random()   #0-1之間隨機亂數
# print(data)

# data=random.uniform(90,180)
# print(data)

# data=random.normalvariate(-5,5)
# print(data)
import statistics as stat
data=stat.mean([2,3,5,8])
data=stat.median([3,5,6,7,8,9,12,3,5,5,100])
data=stat.stdev([3,5,6,7,8,9,10,11,100])
print(data)