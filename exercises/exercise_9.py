"""Remove duplicates from a list:
 Write a Python program that asks the user to enter a list of numbers,
 and then removes any duplicates from the list and prints the resulting list"""

numbers = input("Enter a list of numbers separated by spaces: ")

#Split the numbers into a list
numbers_list = numbers.split()

#Converts the strings to integers
numbers_list =[int(x) for x in numbers_list]

#Removes duplicates from the list using the "set() function"
numbers_list = list(set(numbers_list))

print("The resulting list is: ", numbers_list)
