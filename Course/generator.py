#定義建立生成器函式
# def test():
#     yield 5
# gen=test()    #呼叫並回傳生成器
# print(gen)    #印出<generator object test at 0x0000021CD3284EB0>
# #搭配for迴圈使用印出5
# for d in gen:
#     print(d)

# def test():
#     print("Step 1")
#     yield 5
#     print("Step 2")
#     yield 10
# gen=test()
# for data in gen:
#     print(data)
# def evengenerate(maxnumber):
#     number=0
#     while number<maxnumber:       #無窮迴圈
#         yield number
#         number+=2
# evengenerator=evengenerate(100)
# for data in evengenerator:
#     print(data)
# while True:
#     print("How is your day?")
#     your_reply= input()
#     if your_reply=="good":
#         break
# print("good boy")

# i=0
# while i<6:
#     print(i)
#     i+=1
# else:
#     print("I can only count to 5")
while True:
    print("姓名:")
    name=input()
    if name != "顏貽麟":
        continue
    print("電話:")
    Password=input()
    if Password == "0916189331":
        break
print("你答對了")
