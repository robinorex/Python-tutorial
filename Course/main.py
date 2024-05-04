#封包的用法 要設一個資料夾geo 裡面要有一個空檔案_init_.py  
import geo.point
result=geo.point.distance(2,3)   #呼叫函式
print("距離",result)

import geo.line
result=geo.line.len(2,5,8,9)
print("長度",result)
