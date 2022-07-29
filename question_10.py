# Write a do-while loop that ask a user to enter two numbers .The number should be added and the sum display .The loop should ask the user whether he or she wants to perform the operation again.if so,the loop should reapeate;otherwise it should terminate 

x=int(input("enter a number"))
y=int(input("enter a number"))
q=x+y
print(q)
z="yes"
user_input=int(input("Enter yes , only if you want to perform the operation again"))
while (user_input==z) :
    
    
