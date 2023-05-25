#Write a Python program to get unique values from a list 
my_list = [10, 20, 30, 40, 20, 50, 60, 40]
list = []
for i in my_list:
    if i not in list:
        list.append(i)
print(list)
                