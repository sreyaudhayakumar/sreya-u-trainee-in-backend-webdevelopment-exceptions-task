"""1.Write a Python program that prompts the user to enter an integer and
handles the ValueError exception if the user enters a non-integer value."""

try:
    user_input = int(input("Enter an integer value: "))
    print(user_input)
except ValueError:
    print("Value error! Please enter an integer value.")
finally:
    print("Done")

    
    