# x=[]
# for n in range(10):
#     x.append(n**2)
# print(x[::-2])
# print(x[-2:])


# x=[]
# for n in range(15):
#     if n%2==1:
#         x.append(n**2)
#     else:
#         x.append(n)
# print(x)
# total=0
# items=[3,12,5,6,8,9,10,244,36]
# price=[200,6300,234,555,234,555,23,3,5]
# for i in range(len(items)):
#     # print(items[i],price[i])
#     print(f"{i+1}){items[i]}x{price[i]}={items[i]*price[i]}")
#     total+=items[i]*price[i]
# print(f"total={total}")
# print(list(zip(items,price)))


# # x=10
# # y=3
# # print(f"{x}+{y}={x+y}")
# #99乘法表
# # for j in range(1,10):
# #     for i in range(1,10):
# #         print(f"{j}x{i}={j*i}",end='\t')    #\t代表固定間隔tab
# #     print()

# # var="male",18,190,3,5,6,7,8
# # gender,age,height,*_=var
# # print(gender,age,height)
# # print(gender)
# # print(_)    #*_=*others

# # print("相加 : 10+3=",10+3)
# # print("相減 : 10-3=",10-3)
# # print("相乘 : 10*3=",10*3)
# # print("相除 : 10/3=",10/3)
# # print("整除 : 10//=",10//3)
# # print("取餘數 :10%3=",10%3)
# # print("次方 : 10**3=",10**3)
# count=10
# print("I have " + str(count)+ " " + "apple" )
# print(f"I have {count} apple")
# a=10
# # a+=100  #a=a+100
# a-=6
# print(a)

# username="user"
# password="user"
# vip_level=150
# if username=="admin" and password=="user":
#     print("admin log in")
# elif username=="user" and password=="user":
#     print("log in",end=" ")
#     if vip_level !=0:
#         if vip_level>15:
#             print("diamond")
#         elif vip_level>10:
#             print("second")
#         elif vip_level>5:
#             print("third")
#         elif vip_level>0:
#             print("fourth")
#     else:
#         print("normal vip")
# else:
#     print("no log in")

# def squre_are(width):
#     return width**2 
# def rect_area(width,height):
#     return width*height
# def circle_area(r, angle):
#     return r**2*3.14*angle/360
# area=circle_area(10,180)
# print(area)

# def methond(d):
#     pass
# print("a")

# def methond(a,*args,**kwargs):
#     return (a,args, kwargs)
# print(methond("hi",1,2,3,4,5,6,width=1,height=3))
# def rect_area(width,height):
#     return width*height
# # rect_area_lambda= lambda width, height: width*height
# rect_area_lambda=lambda x,y:x*y
# print(rect_area_lambda(30,40))
import random
def bubble_sort(arr):
    n=len(arr)
    for j in range(n):
        for i in range(0,n-j-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1]= arr[i+1],arr[i]
arr=[]
for i in range(10):
    arr.append(random.randint(0,99))   #產生亂數塞進A陣列
print(arr)
# bubble_sort(arr)
arr.sort()
print(arr)
print(random.randint(0,4))