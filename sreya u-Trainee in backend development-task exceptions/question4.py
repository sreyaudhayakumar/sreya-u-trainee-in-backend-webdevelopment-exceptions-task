"""4.Create a program that attempts to connect to a website and
prints the HTML content if successful.
Use a try-except-else block to handle the requests.exceptions.RequestException exception and 
display an error message if the connection fails."""

import requests

try:
    url = input("Enter the URL of the website: ")  
    response = requests.get(url)
    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print("Failed to connect to the website:", e)

else:
    print("Connection successful!")
    print("HTML content:")
    print(response.text)
