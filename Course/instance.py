#實體物件的建立與使用
class Point:   #Point實體物件的設計:平面座標上的點
    def __init__(self,x,y):  #兩條底線
        self.x=x
        self.y=y
p1=Point(3,4)    #建立實體物件
print(p1.x,p1.y)
p2=Point(5,6)
print(p2.x,p2.y)
p3=Point(123,33)
print(p3.x,p3.y)

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
# p1=Point()
# print(p1.x,p1.y)

class Fullname:
    def __init__(self, first, last):
        self.first=first
        self.last=last
name1=Fullname("Robin","Yen")
print(name1.first,name1.last)
name2=Fullname("Kobe","Lin")
print(name2.first,name2.last)

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):         #定義實體方法
        print(self.x,self.y)
    def distance(self,targetx,targety):
        return ((self.x-targetx)**2+(self.y-targety)**2)**0.5
p=Point(3,4)  #呼叫初始化函式x,y
p.show()   #呼叫實體方法(函式)
result=p.distance(0,0)   #計算(3,4)到原點之間的距離
print(result)

class File:
    def __init__(self,name):
        self.name=name
        self.file=None  #尚未開啟檔案 初期叫None
    def open(self):
        self.file=open(self.name,"r",encoding="utf-8")  #開啟檔案
    def read(self):
        return self.file.read()  #讀取檔案
f1=File("data.text1")  #呼叫初始化函式
f1.open()
print(f1.read())
f2=File("data.text")
f2.open()
print(f2.read())
f3=File("data.text2")
f3.open()
print(f3.read())
