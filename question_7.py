# Write a program that read a set of integer.and print the sum of even and odd integer
# x=int(input("Enter any number"))
# if x% 2==0:
#     print(x,"is an even number")
# elif x>1:
#     for i in range(2,x):
#         if (x% i!=0):
#             print(x,"is a prime number")
#             break
    

list=[1,2,3,4,5,6,7,8,9,11,10]
print("Even and odd set numbers", list)
even=0
odd=0

for i in list :
    if (i % 2==0):
        even= even + i
    else:
        odd=odd+ i

print(even)
print(odd)
    

 
   


   
