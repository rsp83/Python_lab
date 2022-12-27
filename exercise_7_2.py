"""
    7.Calculate the average of a list of numbers:
     Write a Python program that asks the user to enter a list of numbers
     and then calculates and prints the average of those numbers"""
#declare the function
def average(numbers):

    sum = 0
    for number in numbers:
       sum += number

#calculate the average by dividing the sum by the lenght of the list
    average = sum / len(numbers)

    return average


#get the list and converts it using functions rather them a a for in loop
numbers = list(map(int, input("enter a list of numbers separated by space").split()))

avg = average(numbers)
print(f"The average of the numbers is: {avg}")



