"""Calculate the factorial of a number:
 Write a Python program that asks the user to enter a number
 and then calculates and prints the factorial of that number."""

 def factorial(n):
    result = 1
    for i in range (1, n+1):
        result *= i
    return result

    num = int(input("Enter a number: "))

