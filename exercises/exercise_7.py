"""
    7.Calculate the average of a list of numbers:
     Write a Python program that asks the user to enter a list of numbers
     and then calculates and prints the average of those numbers"""
#declare the function
def calculate_average(function_numbers):
    """Calculates the average of a list of numbers.

    Args:
    numbers (list): A list of numbers to calculate the average of.

    Returns:
    float: The average of the numbers."""

#Initialize a variable to store the sum
    total_sum = 0


#iterate over the elements of the list
    for number in function_numbers:
        #add the current element to the sum
        total_sum += number
#calculate the average by dividing the sum by the lenght of the list
    average = total_sum / len(function_numbers)

    return average


#get the list
input_numbers = input("enter a list of numbers separated by space")

#separate the numbers into a list
input_numbers = [int(x) for x in input_numbers.split()]

avg = calculate_average(input_numbers)
print (f"the average of the numbers is: {avg}")
