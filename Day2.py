 # for x in "banana":
 #      print(x, end="")

# print(type(x))
     

 # for i in range(10): # 0 to n-1 range
 #     print(i)

 # for i in range(2,9):  # 2 to 8
 #     print(i)

 # for i in range (2,9,3):  # 2 to 8 and increment by +3
 #      print(i)

# sum = 0
# for i in range(6):
#       sum +=i    # sum + = i is wrong

# print(sum)

# sum = 0
# print("Enter the range")
# n = int(input())
# for i in range (n+1):
#      sum+=i

# print(sum)

# i=0
# while (i <=10):
#       if(i==6):
#             break
#       i+=1
#       print(i)
# print(i)

# for i in range(1,10):
#          if(i==5 or i==7):
#                continue
#          print(i)


# j=0
# while(j<=6):
#       j+=1
#       if(j==4):
#         continue
#       #j+=1
#       print(j)   # it will do infinite loop because after j=4 the loop will terminate and 
#       #i value will be 4 and again it will do continue again it will terminate 

# k=0
# while (k<=10):
#       k+=1
#       if(k==5 and k==7):
#             continue
#       print(k)



for i in range(1,6):
      for j in range(1,4):
            print(i+j, end=" ")
      print(" ")

i=0
n= int(input("Enter range"))
sum= 0
while(i<=n):
      sum+=i
      i+=1
print(sum//n)


