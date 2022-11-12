# math is imported to make use of other library modules, especially maths module:
# especially of the fact that calculating the area of square, rectangle and circle were or are concern
import math

# the variable 'shape_of_building' was initialized requesting the user to enter the shape of the building.
# the .lower() is added to the end of a python string value
# the python lower() method converts all characters in a string to lowercase.
# NB: Numbers and special characters are left unchanged. The loer() function takes in parameters
# the variable shape_of_building is printed

shape_of_building = input("enter the shape of building: square, rectangle or round: ").lower()
print(shape_of_building)

# the if and elif conditions are used to compare the area square, rectangle and round based on user choice.

# the if conditional statement used to compare shape_of_building to the value square
if shape_of_building == 'square':

    # sides are casted to integer to assure a smooth calculations.
    # since in the case of square sides are equal we got to use (side)**2
    side = int(float(input("Enter the side of the building:\n")))
    area = (side)**2

    # area printed
    print(f'The area of the building is: {area}')

# the_shape_of-building is used to compared the it to the value rectangle before establishing it width and length sides
elif shape_of_building == 'rectangle':

    # two sides are mention because rectangles the length and width have different dimensions
    # the values of sides  are casted into an integer.
    side1 = int(float(input("enter the first side of the buildings:\n")))
    side2 = int(float(input(" enter the second side of the building:\n")))

# the area is side1 multiplied by side2
    area = side1*side2

# using the function to print the area
    print(f'the area of the building is: {area}')

# since we are comparing, elif is still useful here
# shape_of_building is compared to round.
# == used because the value is a string
elif shape_of_building == 'round':

    # user requested to enter the area and the value is casted
    area = int(float(input("enter the the area of the building")))

    # area printed
    print(area)

    # the area of circle is calculated with the help of the math modules imported
    area_of_circle = math.pi * math.pow(area,2)

    # thus area printed
    print('The area of the circle is: %.2f' % area_of_circle)


