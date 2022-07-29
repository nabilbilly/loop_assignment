# write a program to write a number tell a user want and at the end the program should the largest and the smallest entered.
number_1=int(input("enter your First number : "))
number_2=int(input("enter your Second number : "))
number_3=int(input("enter your Third number : "))
if number_1 > number_2 and number_1 > number_3:
    print(number_3, "is the greatest")
    if number_2 < number_3:
        print(number_2, "is the smallest")
    elif number_2 == number_3:
        print( number_2, "and" ,number_3 ,"are equal")
    else:
        print(number_3, "is the smallest")
if number_2 > number_1 and number_2 > number_3:
    print(number_2, "is the greatest")
    if number_1 < number_3:
        print(number_1, "is the smallest")
    elif number_1 == number_3:
        print(number_1, "and" ,number_3 ,"are equal")
    else:
        print(number_3, "is the smallest")
if number_3 > number_2 and number_3 > number_1:
    print(number_3, "is the greatest") 
    if number_1 < number_2:
        print(number_1, "is the smallest")
    elif number_1== number_2:
        print(number_1, "and" ,number_2 ,"are equal")
    else:
        print(number_2, "is the smallest")
elif number_1 == number_2 and number_1 == number_3:
    print( "all are equal")
    