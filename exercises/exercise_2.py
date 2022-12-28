"""Exercise 2
    Convert Celsius to Fahrenheit:
     Write a Python program that asks the user to enter a temperature in Celsius
      and then converts and prints the temperature in Fahrenheit."""


#asks the user to enter a temperature in Celsius
celsius = input("Hello!, what is the temperature now in Celsius ?")

#string to float number
celsius = float(celsius)

#converts and prints the temperature in Fahrenheit
fahrenheit = celsius * 9/5 + 32
print("the converted value of Celsius \
     to Fahrenheit is : " + str(fahrenheit) +", thank you for using this proggramm")
