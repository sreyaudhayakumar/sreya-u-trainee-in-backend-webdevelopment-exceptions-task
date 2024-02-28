"""9.Write a Python program that prompts the user to enter their age.
Define a custom exception called InvalidAgeError that 
is raised when the entered age is less than 0 or 
greater than 150. Handle the InvalidAgeError exception and
display an appropriate error message.""" 

class InvalidAgeError(Exception):
    pass

age = int(input("Enter your age: "))

try:
    if age < 0 or age > 150:
        raise InvalidAgeError("Age must be between 0 and 150")
    else:
        print("Your age is:", age)
except InvalidAgeError as e:
    print("Error:", e)