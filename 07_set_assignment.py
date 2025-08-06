# SET DATATYPE ASSIGNMENT
# ======================

# SOLVED EXAMPLE
# --------------
# Question: Find the union of two sets
print("SOLVED EXAMPLE:")
print("Find the union of two sets")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {union_set}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create a set of first 10 natural numbers
print("Question 1: Create a set of first 10 natural numbers")
# Your code here
numbers = set(range(0,11))
print(numbers)

# Question 2: Add element 11 to set {1, 2, 3, 4, 5}
print("\nQuestion 2: Add element 11 to set {1, 2, 3, 4, 5}")
# Your code here
set1 = {1,2,3,4,5}
set1.add(11)
print(set1)

# Question 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}
print("\nQuestion 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}")
# Your code here
set1 = {1,2,3,4,5,6}
set1.remove(3)
print(set1)

# Question 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
print("\nQuestion 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
# Your code here
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1 & set2)

# Question 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
print("\nQuestion 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
# Your code here
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1.difference(set2))


# Question 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}
print("\nQuestion 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}")
# Your code here
set1 = {1,2,3,4,6,7,8}
print(5 in set1)


# Question 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}
print("\nQuestion 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}")
# Your code here
set1 = {'a', 'b', 'c', 'd', 'e'}
print(len(set1))

# Question 8: Create a set of vowels from string "hello world"
print("\nQuestion 8: Create a set of vowels from string 'hello world'")
# Your code here
string = "hello world"
vowels = {'a','e','i','o','u'}
vowel_set = set()
for i in string:
    if i in vowels:
        vowel_set.add(i)
print(vowel_set)

# Question 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] using set
print("\nQuestion 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] using set")
# Your code here
numbers = [1,2,2,3,4,4,5,6,6,7]
print(set(numbers))

# Question 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}
print("\nQuestion 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}")
# Your code here 
a = {1, 2, 3}
b = {1, 2, 3, 4, 5, 6}

print(a.issubset(b))