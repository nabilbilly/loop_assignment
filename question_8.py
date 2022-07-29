# Write A Program that Prompt the user to input a positive integer it should than output a message indicating whether is a prime number
x=int(input("enter a positive number"))
if x>0:
    for i in range(1,x):
         if (x% i!=0):
            print(x,"is a prime number")
            break
else:
    print("it is not a prime number for Real!")
            
    

        


