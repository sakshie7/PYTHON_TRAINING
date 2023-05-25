#Write a Python program to returns sum of all divisors of a number.
number = int(input("Enter a number: "))

divisors = []
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

divisor_sum = sum(divisors)
print("Sum of divisors:", divisor_sum)
