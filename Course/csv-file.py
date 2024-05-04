# import csv
# # with open("data.csv","w",newline="") as file:
# #     writer=csv.writer(file)    #建立物件
# #     writer.writerow([1,2,3])
# #     writer.writerow([4,5,6])
# #     writer.writerow([7,8,9])
# with open("data.csv","r",newline="") as file:
#     reader=csv.reader(file)
#     total=0
#     for row in reader:
#         for number in row:
#             total+=int(number)
#     print(total)

import numpy as np
x=np.array([[0,1,2],[2,3,4],[4,5,6],[6,7,8],[8,9,10]])
print(x[:,0])
print(x[:,1])
print(x[:,2])
print(x[1,:])
        