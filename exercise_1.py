'''
exercise_1
Calculate the area of a rectangle:
Write a Python program that asks the user to enter the width and height of a rectangle
and then calculates and prints the area of the rectangle
'''


#get the user to enter the width of a rectangle
width = input("What is the width ?")
print("Good, the width is " + width )


#get the user to enter the height of a rectangle
height = input("What is the height ?")
print("Good, the height is " + height )


#convert height and width to floating point numbers
height = float(height)
width = float(width)


#calculates area
area = height * width
print("the area of this retangle is equal to " + str(area) + ",thank you for using my programm")
