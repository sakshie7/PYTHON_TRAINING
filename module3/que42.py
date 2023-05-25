# Write a Python program to print all unique values in a dictionary.
my_dicto={
    "group a" : 70,
    "group b" : 80,
    "group c" : 50,
    "group a" : 70,
    "group c" : 50
}

unique_values = set(my_dicto.values())

print("Unique values in the dictionary:")
for value in unique_values:
    print(value)