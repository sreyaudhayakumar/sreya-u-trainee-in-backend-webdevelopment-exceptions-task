"""2.Create a program that opens a file and reads its contents. 
Use a try-except block to handle the FileNotFoundError exception and display a custom error message
if the file does not exist."""

try:
    file = open("sreya u-Trainee in backend development-task exceptions/demo.txt", 'r')
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found! Please make sure the file exists.")
