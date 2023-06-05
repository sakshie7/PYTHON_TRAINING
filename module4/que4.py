#Write a Python program to read first n lines of a file.
f = open("terms.txt","r")
n = int(input("Enter the number of lines to read: "))
l1 = f.readlines()[:n]
for i in l1:
    print(i)


