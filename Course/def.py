# def multiply(n1,n2,n3):  #定義函式function
#     result=n1*n2*n3
#     print(result)   
# multiply(2,3,5)  #呼叫函式


# def say(msg):
#     print(msg)
#     return "hi"   #回傳值
# value=say("hello")
# print(value)

# def multiply(n1,n2,n3):
#     result=n1*n2*n3
#     return(result)
# value=multiply(3,4,7)+multiply(6,12,8)+multiply(7,10,11)
# print(value)

#函式的包裝
# def calculate(max):   #define
#     sum=0
#     for n in range(max+1):
#         sum=sum+n
#     print(sum)
# calculate(10)
# calculate(1000)


# def say(*msgs):
#     for msg in msgs:
#         print(msg)
# say("hello","abritiriage","1","2","3")

# def power(base,exp=0):
#     print(base**exp)
# power(3,3)
# power(6)

# def divide(n1,n2):
#     print(n1/n2)
# divide(2,4)
# divide(n2=2, n1=4)

#Tuple: a list with order 
def avg(*ns):    #無限參數資料 列表上加個*
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns))   #len就是列表的個數(長度)
avg(3,4,5,6)
avg(3,4,5,-8,-4,0)
avg(123123,4,68304,4)

# def avg(*ns):
#     for n in ns:
#         print(n)
# avg(3,4,5,-8,-4,0)

def avg(*ns):
    for n in ns:
        print(n)
avg(2,3)