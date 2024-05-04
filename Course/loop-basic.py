#while loop
#n=1
#while n<=5:
#    print(n)
#    n+=1

#n=1
#sum=0
#while n<=10:
#    sum=sum+n
#    n+=5
#print(sum)

#for loop
#for x in [1,3,5,7,9]:
#    print(x)

#for x in [1,3,4,5]:
#    print("1",x)
#for c in "hello":
 #   print("hey",c)
#for x in range(5):  #range(5) 就是[0,1,2,3,4]的意思
 #   print(x)
#for x in range(1,6):   #[1,2,3,4,5]
#    print(x)
#for x in range(1,21,2):  
#    print(x)
# sum=0
# for x in range(999):
#     sum=sum+x
# print(sum)
def countLetters(word):
    count=0
    for x in word:
        if x.isalpha():
            count+=1
    return count
print(countLetters("pythonsdfaafadfaf"))
