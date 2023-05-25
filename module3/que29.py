# Write a Python program to unzip a list of tuples into individual lists.
my_list=[(10,'a'),(30,'b')]
unzip=list(zip(*my_list))
print(unzip)
