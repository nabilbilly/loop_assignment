# write a program to calculate the factorial value of any number entered from the keyboard.
print("This Will Help find The Factorial Of Any Number You Enter ") 
x=int(input("Enter a number: "))
f=1
for num in range(1,x+1):
    f=f*num

print(f)
