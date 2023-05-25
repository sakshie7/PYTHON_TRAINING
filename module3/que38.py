 #Write a Python program to check multiple keys exists in a dictionary

my_list={
       

    "key1": 10,
    "key2": 20,
    "key3": 30,
    "key4": 40
}

keys_to_check = ["key1", "key3", "key5"]

all_keys_exist = True

for key in keys_to_check:
    if key not in my_list:
        all_keys_exist = False
        break

if all_keys_exist:
    print("All keys exist in the dictionary")
else:
    print("Some keys do not exist in the dictionary")
