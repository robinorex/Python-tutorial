def mydecofactory(base):     #裝飾器工廠的彈性在於參數的加入 如base
    def myDeco(callback):
        def run():
            print("inner function",(base+4)*62)
            result=base**3
            callback(result)
        return run
    return myDeco

@mydecofactory(78)
def test(result):
    print("callback function",result)
test()

#1+2+3+.......+max的裝飾器工廠
def calculatefactory(max):
    def calculate(callback):
        def run():
            total=0
            for n in range(max+1):
                total+=n
            callback(total)
        return run
    return calculate
@calculatefactory(1000)    #參數變動在factory這
def test(result):
    print("result",result)
test()
