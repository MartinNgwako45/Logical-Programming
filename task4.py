# asking the user to enter an integer
num1 = int(input("enetr an integer"))
print(num1)

# determine if the users input is divisible by 2 and 5 
if ((num1 % 2) == 0 ) and ((num1 % 5) == 0):
    print("is divisible by 2 and 5".format(num1))
else :
# displying the result 
    print("is not divisible by 2 and 5".format(num1))

if ((num1 % 2) == 0 ) or ((num1 % 5) == 0):
    print("is divisible by 2 or 5".format(num1))
else :
    print("is not divisible by 2 or 5".format(num1))

