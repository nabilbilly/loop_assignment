# write a program to calculate the HCF of two numbers
from re import X


x=100
y=86
if x >y:
    smaller=y
else:
    smaller=x 

for i in range(1,smaller+1):
    if ((x %  i==0) and (y % i==0)):
        hcf=i
        print(i)



