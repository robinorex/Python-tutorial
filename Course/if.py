#y=input("請輸入數字: ")
#y=int(y)
#if y>200:
 #   print("大於200")
#elif y>100:
#    print("大於100小於200")
#else:
#    print("小於等於100")
n1=int(input("please put number1: "))
n2=int(input("please put number2: "))
print(n1+n2)
op=input("請輸入運算: +,-,*,/ ")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("unreasonable")


