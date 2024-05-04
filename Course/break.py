#n=1  
#while n<5:
#    if n==3:
#        break
#    n=n+1   #n+=1 等於 n=n+1 or num=num+1
#print("hello",n)

# n=0
# while n<5:
#     if n==3:  # 迴圈裡n= 0, 1, 2, 3的意思
#         break
#     print(n)  #迴圈中的n
#     n+=1 
# print("最後的n:",n)  #迴圈最後的n=3就要停了

# n=0
# while n<8:
#     print(n)
#     n+=1
# print("last n:",n) 
    
#Continue loop
# n=0
# for x in [0,1,2,3]:
#     if x%2==0:
#         continue  #遇到continue if TRUE 則跳過下方程式繼續跑回圈
#     print(x)     #回圈內只會print出1,3  加兩次所以最後印出來是2
#     n+=1
# print(n)

# sum=0
# for n in range(1000):
#     sum=sum+n   #sum+=n
# else:
#     print(sum)

# n=int(input("輸入的數字: "))
# for i in range(n):   #0~n-1
#     if i**2== n:     #要記得兩個==
#         print("整數平方根", i)
#         break    #break出現就不會執行下方程式
# else:
#     print("not available")

n=int(input("put the number: "))
for i in range(n):
    if i*i==n:
        print("correct", i)
        break
else:
    print("no")
