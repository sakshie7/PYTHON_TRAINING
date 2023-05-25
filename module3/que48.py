#Write a Python function to check whether a number is perfect or not.
def is_perfect_number(number):
   
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i

    return number == divisor_sum
num = int(input("Enter a number: "))
result = is_perfect_number(num)
if result:
    print("The number is a perfect number.")
else:
    print("The number is not a perfect number.")


