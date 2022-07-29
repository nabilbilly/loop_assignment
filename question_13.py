# write a program to print the fibbonacci of n terms where n is input by user
number=int(input("Enter a number")) 
x=0
y=1
sum=0
for i in range(0,number):
    print(x, end ='')
    sum=sum +x
    next=x+y
    x=y
    y=next
print(sum)