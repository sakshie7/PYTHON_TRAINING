# take input from the user
num = int(input("Enter a number: "))
# check if the number is negative or positive
if num < 0:
    print("Factorial cannot be found for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    numb = 1
    for i in range(1, num+1):
        facto = numb * i
    print("Factorial of", num, "is", numb)
