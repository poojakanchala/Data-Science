# INTEGER DATATYPE ASSIGNMENT
# ===========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the sum of first 5 even numbers
print("SOLVED EXAMPLE:")
print("Calculate the sum of first 5 even numbers")
first_5_even = [2, 4, 6, 8, 10]
sum_even = sum(first_5_even)
print(f"First 5 even numbers: {first_5_even}")
print(f"Sum: {sum_even}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the product of first 10 natural numbers
print("Question 1: Calculate the product of first 10 natural numbers")
# Your code here
num = 10
product = 1
for i in range(1,num+1):
    product = product * i
print(product,end =' ')



# Question 2: Find the remainder when 156 is divided by 7
print("\nQuestion 2: Find the remainder when 156 is divided by 7")
# Your code here
a = 156
b = 7
print(a%b)

# Question 3: Calculate the square of 25
print("\nQuestion 3: Calculate the square of 25")
# Your code here
n = 25
print(n**2)

# Question 4: Find the cube root of 125
print("\nQuestion 4: Find the cube root of 125")
# Your code here
n = 125
print(n**(1/3))

# Question 5: Calculate the sum of digits in number 12345
print("\nQuestion 5: Calculate the sum of digits in number 12345")
# Your code here
nums = [1,2,3,4,5]
sum = 0
for i in nums:
    sum += i
print("sum of digits= ",sum)



# Question 6: Check if 97 is a prime number
print("\nQuestion 6: Check if 97 is a prime number")
# Your code here
num = 97
for i in range(2,num):
    if (num%i == 0):
        print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")


# Question 7: Find the factorial of 8
print("\nQuestion 7: Find the factorial of 8")
# Your code here
num = 8
fact = 1
for i in range(1,num+1):
    fact *= i
print("factorial of 8 is = ", fact)


# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56
print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")
# Your code here
nums = [15,23,31,42,56]
sum = 0
avg = 0
for i in nums:
    sum += i
avg = sum/len(nums)
print(avg)

# Question 9: Find the greatest common divisor (GCD) of 48 and 36
print("\nQuestion 9: Find the greatest common divisor (GCD) of 48 and 36")
# Your code here
a = 48
b = 36
gcd = 1
for i in range(1,min(a,b)+1):
    if a % i == 0 and b % i == 0:
        gcd = i
print(gcd)

# Question 10: Calculate the sum of first 20 odd numbers
print("\nQuestion 10: Calculate the sum of first 20 odd numbers")
# Your code here 
num = 20
sum = 0
for i in range(0,num*2):
    if i%2 != 0:
        sum += i
print(sum) 