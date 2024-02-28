"""3.Write a program that calculates the division of two numbers entered by the user. 
Use a try-except block to handle the ZeroDivisionError exception and display an appropriate error message 
if the user tries to divide by zero."""

try:
    user_input = int(input("Enter the first number: "))
    user_input2 = int(input("Enter the second number: "))
    output = user_input / user_input2
    print("Result:", output)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
