"""5.Write a program that opens a file, reads its contents, 
and writes the contents to a new file. Use a try-except-finally block to ensure that the file is closed even if 
an exception occurs during the file operations."""

try:
    with open(r"sreya u-Trainee in backend development-task exceptions\demo.txt", 'r') as source_file:
        contents = source_file.read()

    with open(r"sreya u-Trainee in backend development-task exceptions\destination_file.txt", 'w') as destination_file:
        destination_file.write(contents)

except Exception as e:
    print("An error occurred:", e)

finally:
    print("File operations complete.")
