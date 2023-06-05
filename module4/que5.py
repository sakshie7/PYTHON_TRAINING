#Write a Python program to read last n lines of a file.
f = open("terxm.txt","r")
n = int(input("Enter the number of lines to read: "))
l1 = f.readlines()[n:]
for i in l1:
    print(i)