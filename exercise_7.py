"""
    7.Calculate the average of a list of numbers:
     Write a Python program that asks the user to enter a list of numbers
     and then calculates and prints the average of those numbers"""
#declare the function
def average(numbers):

#Initialize a variable to store the sum
    sum = 0


#iterate over the elements of the list
    for number in numbers:
        #add the current element to the sum
        sum += number
#calculate the average by dividing the sum by the lenght of the list
    average = sum / len(numbers)

    return average


#get the list
numbers = input("enter a list of numbers separated by space")

#separate the numbers into a list
numbers = [int(x) for x in numbers.split()]

avg = average(numbers)
print (f"the average of the numbers is: {avg}")


