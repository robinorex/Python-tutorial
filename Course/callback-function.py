def test(arg):
    arg("hello")     #呼叫回呼函式
def handle(data):    #定義一個回呼函式
    print(data)
test(handle)

def multiply(n1,n2,n3,cb):
    cb(n1*n2*n3)
def handle1(result):
    print(result)
multiply(12,33,67,handle1)

def subtract(n1,n2,n3,cb1):
    cb1(n1-n2-n3)
def handle2(result):
    print(result)
def handle3(result):
    print("result is",result)
subtract(1923,3362,86,handle2)
subtract(23423,3453496,14434,handle3)