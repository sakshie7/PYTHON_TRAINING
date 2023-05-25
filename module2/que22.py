string = "patelsakshi"
string1=input("enter a string")

if len(string1) < 2:
    result = " "
else:
    result = string[:2] + string[-2:]

print("The result is:", result)
