#Write a Python program to read a file line by line store it into a variable.
file_path = "term2.txt"
n = int(input("Enter the number of lines to read: "))
file = open(file_path, "r")
lines = file.readlines()
file.close()
lines = lines[:n]  
print(lines)