# Write a Python program to check whether a list contains a sub list
list=[10,20,30,40,50,60]
l2=[10,20,30]

if all(elem in list for elem in l2):
    print("list is true")
else:
    print("list is false")    
    
