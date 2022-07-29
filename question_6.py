#   Write a program which prompt a use to input a number and output the number with a digital reverse
print("This will Get the Reverse Of Any Series Of Number You Enter. Eg  123 -321 ")
y=int(input("Enter A Series Of Positive  Number :"))
rev=0
while y >0:
    rev=(rev*10) + (y %10)
    y=y //10

print("The reversed outcome is",rev)