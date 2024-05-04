# data=input("Please insert a number: ")
# try:    #認知哪段程式有可能有例外
#     number=int(data)
# except Exception:
#     number=0
# number=number*2
# print(number)

# while True:
#     data=input("Please insert a number: ")
#     try:                    #認知哪段程式有可能有例外
#         number=int(data)
#         break
#     except Exception:
#         print("Wrong format Please insert again")
# number=number*2
# print(number)

while True:
    name=input("Name: ")
    if name != "Robin":
        continue
    Password=input("password: ")
    if Password=="123":
        break
print("correct")
