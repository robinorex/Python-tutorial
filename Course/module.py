# import sys
# print(sys.platform)
# print(sys.maxsize)
# print(sys.path)

# import geometry
# result=geometry.distance(2,3,8,9)
# print(result)

# import geometry
# result=geometry.slope(212,354,878,885)
# print(result)

import sys
sys.path.append("modules")  #調整(新增)搜尋模組的路徑 因為我新創了一個modules表格
print(sys.path)                           #把geometry放進modules表格裡面 換路徑
print("-----------------------")
import geometry
print(geometry.distance(2,3,3,4))
print(geometry.slope(1,5,2,3))
print(sys.maxsize)