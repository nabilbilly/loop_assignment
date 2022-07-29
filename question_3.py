# write a program that prompt a user to input a positive integer.it should then print the multiplication table of that number
print("Get The Multiplication Timetable Of any Positive number You Enter ")
num=int(input("please enter a positive number of your choice: "))
y=int(input("Please enter Your your 1st Range 0f number: eg, from  "))
z=int(input("Please enter Your your 2st Range number:eg to  "))
for count in range(y,z):
    print(num,'x',count,'=',num*count)
5