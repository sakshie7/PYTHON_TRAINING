#Write a Python program to map two lists into a dictionary
keys = ["key1", "key2", "key3"]
values = [10, 20, 30]

my_dict = {k: v for k, v in zip(keys, values)}

print(my_dict)
