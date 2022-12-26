"""Exercise 3
    Find the largest number:
    Write a Python program that asks the user to enter three numbers
    then prints the largest of the three numbers."""

num1 = int(input("Please enter a number"))
num2 = int(input("Please another one"))
num3 = int(input("last one, and i will tell you wich one is the largest"))


largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

print(largest)
