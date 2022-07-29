# write a program to read the numbes till the user wants and at the end it should display the counts of positive,negative and zero 
print("This program will determine whether the number you entered is positiv , negative or zero")
x=float(input("Enter a number : "))
if x >0:
    print(x, "is a POSITIVE NUMBER")
elif x< 0:
    print(x, ("is a NEGATIVE NUMBER"))
else:
    print(x, "is ZERO")