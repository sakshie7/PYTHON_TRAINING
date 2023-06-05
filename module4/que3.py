#Write a Python program to append text to a file and display the text.

# Open the file in append mode
file1 = "myblank_file.txt"
file = open(file1, "a")

# Ask the user for text to append
name = input("Enter the Data: ")

# Append the text to the file
file.write(name + "\n")  # Add a new line after each appended text

# Close the file
file.close()


