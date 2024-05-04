# #定義裝飾器
# def myDeco(callback):     #裝飾器名稱
#     def run():                     #定義內部函式
#         print("裝飾器中的程式碼")
#         callback(3)    #這個回乎函式 就是下面的被裝飾函式 參數從這邊控制
#     return run    #return內部函式
# #使用裝飾器
# @myDeco
# def test(n):                          #這個其實就是callback function
#     print("普通函式程式碼",n)
# test()
def calculate(callback):
    def run():
        result=0
        for n in range(101):
            result+=n
        callback(result)   #把計算結果透過參數callback到被裝飾的函式中
    return run
@calculate
def show(n):
    print("計算結果",n)
@calculate
def showEng(n):
    print("Result",n)
show()
showEng()
    







# decoratedFunc()  # 大方向 : 先執行裝飾器內部的程式碼再執行本來的程式碼

# 程式範例
# def testDecorator(callback):
#   def innerFunc():
#       print("裝飾器")
#       callback(3)
#   return innerFunc

# @testDecorator
# def decoratedFunc(data):
#   print("普通函式",data)

# decoratedFunc()  
# decoratedFunc()->testDecorator(callback)->執行裝飾器內部程式碼innerFunc()->callback等於decoratedFunc->執行decoratedFunc