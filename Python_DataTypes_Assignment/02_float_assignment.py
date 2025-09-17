# FLOAT DATATYPE ASSIGNMENT
# =========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the area of a circle with radius 5.5
print("SOLVED EXAMPLE:")
print("Calculate the area of a circle with radius 5.5")
import math
radius = 5.5
area = math.pi * radius ** 2
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577
print("Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577")
# Your code here
nums = [3.14,2.718,1.618,0.577]
sum = 0
avg = 0
for i in nums:
    sum += i
avg = sum/len(nums)
print(avg)

# Question 2: Convert 98.6 Fahrenheit to Celsius (F = C * 9/5 + 32)
print("\nQuestion 2: Convert 98.6 Fahrenheit to Celsius")
# Your code here
Fahrenheit = 98.6
Celsius = (Fahrenheit - 32) / (9/5)
print(Celsius)


# Question 3: Calculate the compound interest on $1000 at 5.5% for 3 years
print("\nQuestion 3: Calculate compound interest on $1000 at 5.5% for 3 years")
# Your code here
#CI = A - P, where A = P (1 + (r/100))^t
P = 1000
CI = 0
A = P*(1+(5.5/100))**3
CI = A - P
print(CI)

# Question 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2
print("\nQuestion 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2")
# Your code here
x = 3.5
y = 4.2
z = ((x*x)+(y*y))**(1/2)
print(z)
# Question 5: Calculate the volume of a sphere with radius 7.8
print("\nQuestion 5: Calculate the volume of a sphere with radius 7.8")
# Your code here
radius = 7.8
area = 4*3.14*radius*radius
print(area)

# Question 6: Round 3.14159 to 3 decimal places
print("\nQuestion 6: Round 3.14159 to 3 decimal places")
# Your code here
x = 3.14159
print(round(x,3))
# Question 7: Calculate the percentage: 45 out of 67
print("\nQuestion 7: Calculate the percentage: 45 out of 67")
# Your code here
print((45/67)*100)

# Question 8: Find the square root of 23.456
print("\nQuestion 8: Find the square root of 23.456")
# Your code here
import math
print(math.sqrt(23.456))

# Question 9: Calculate the simple interest: Principal=2500, Rate=6.5%, Time=2.5 years
print("\nQuestion 9: Calculate simple interest: Principal=2500, Rate=6.5%, Time=2.5 years")
# Your code here
SI = (2500*6.5*2.5)/100
print(SI)

# Question 10: Convert 45.7 degrees to radians
print("\nQuestion 10: Convert 45.7 degrees to radians")
# Your code here 
degree = 45.7
radian = degree * (3.14/180)
print(radian)