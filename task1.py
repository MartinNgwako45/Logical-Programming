num1 = 25
num2 = 15
num3 = 5


#comparing num1 and num2 to show the largest value between the two
if(num1>num2):
    print("{0} is greater than {1}".format(num1, num2))
elif(num2>num1):
    print("{0} is greater than {1}".format(num2, num1))


#determining wether num1 is even or odd using the % function
if(num1 % 2)== 0:
    print("{0} is even number".format(num1))
else:
    print("{0} is odd number".format(num1))
    

#sorting the number from the big to small
#using the if statement to check the smallest number out of the three variables
if num1 < num2 and num1 < num3:
    lowest = num1
elif num2 < num1 and num2 < num3:
    lowest = num2
else:
    lowest = num3

#checking if num1  is bigger than num2 and smaller than num3
if num1 > num2 and num1 < num3:
    middle = num1
elif num2 > num1 and num2 < num3:
    middle = num2
    #if num1 and num2 are not the second biggest number that  means that num3 is the second biggest and middle number
else:
    middle = num3
#checking for the biggest  value
if num1 > num2 and num1 > num3:
    highest = num1
elif num2 > num1 and num2 > num3:
    highest = num2
else:   
    highest = num3

#printing out the number from smallest to the biggest
print(lowest, middle, highest)
