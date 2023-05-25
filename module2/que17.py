# Get single string from two given strings, separated by space
string1 = "hello"
string2 = "world"

# Swap first two characters of each string
string1 = string1[1] + string2[1:] + " " + string2[1] + string1[1:]

print(string1)
