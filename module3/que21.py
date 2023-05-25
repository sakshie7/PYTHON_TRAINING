#Write a Python program to convert a tuple to a string.
my_tuple = ('H', 'E', 'L', 'L', 'O', 'W', 'W', 'O', 'R', 'L', 'D', '!')
string_result = ''
for item in my_tuple:
    string_result += str(item)
print(string_result)
