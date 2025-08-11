# LIST DATATYPE ASSIGNMENT - 50 QUESTIONS
# ======================================

# SOLVED EXAMPLE
# --------------
# Question: Find the maximum and minimum values in a list
print("SOLVED EXAMPLE:")
print("Find the maximum and minimum values in a list")
numbers = [23, 45, 12, 67, 34, 89, 56]
max_val = max(numbers)
min_val = min(numbers)
print(f"List: {numbers}")
print(f"Maximum: {max_val}")
print(f"Minimum: {min_val}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Create a list of first 10 square numbers
print("Question 1: Create a list of first 10 square numbers")
# Your code here
num = 10
squares = []
for i in range(1,num+1):
    squares.append(i*i)
print(squares)

# Question 2: Find the sum of all even numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nQuestion 2: Find the sum of all even numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
# Your code here
list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in list:
    if i%2 == 0:
        sum += i
print(sum)

# Question 3: Remove duplicates from [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print("\nQuestion 3: Remove duplicates from [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]")
# Your code here
list = [1,2,2,3,4,4,5,6,6,7]
unique = []
for i in list:
    if i not in unique:
        unique.append(i)
print(unique)

# Question 4: Sort the list [64, 34, 25, 12, 22, 11, 90] in descending order
print("\nQuestion 4: Sort the list [64, 34, 25, 12, 22, 11, 90] in descending order")
# Your code here
list = [64,34,25,12,22,11,90] 
list.sort(reverse=True)
print(list)


# Question 5: Find the average of numbers in [15, 23, 31, 42, 56, 78, 91]
print("\nQuestion 5: Find the average of numbers in [15, 23, 31, 42, 56, 78, 91]")
# Your code here
list = [15,23,31,42,56,78,91]
sum = 0
for i in list:
    sum += i
avg = sum/len(list)
print(avg)


# Question 6: Create a list of first 15 Fibonacci numbers
print("\nQuestion 6: Create a list of first 15 Fibonacci numbers")
# Your code here
fib = [0,1]
n = 15
for i in range(2,n):
    next_term = fib[i-1] + fib[i-2]
    fib.append(next_term)
print(fib)


# Question 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]
print("\nQuestion 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]")
# Your code here
list=[45,67,23,89,12,34,78]
list.sort()
print(list[-2])


# Question 8: Reverse the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nQuestion 8: Reverse the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
# Your code here
list = [1,2,3,4,5,6,7,8,9,10]
list.reverse()
print(list)

# Question 9: Count how many times 5 appears in [1, 5, 2, 5, 3, 5, 4, 5, 6]
print("\nQuestion 9: Count how many times 5 appears in [1, 5, 2, 5, 3, 5, 4, 5, 6]")
# Your code here
list = [1,5,2,5,3,5,4,5,6]
print(list.count(5))


# Question 10: Create a list of prime numbers between 1 and 50
print("\nQuestion 10: Create a list of prime numbers between 1 and 50")
# Your code here
prime = []
for num in range(2,51):
    is_prime = True
    for i in range(2,num):
        if num%i == 0:
            is_prime = False
            break
    if is_prime:
         prime.append(num)
print(prime)

# Question 11: Flatten nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 11: Flatten nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here
list = [[1,2,3],[4,5,6],[7,8,9]]
flatten = []
for item in list:
    for i in item:
        flatten.append(i)
print(flatten)


# Question 12: Find common elements between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8]
print("\nQuestion 12: Find common elements between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8]")
# Your code here
l1 = [1,2,3,4,5,5]
l2 = [4,5,6,7,8]
common = []
for item in l1:
    if item in l2 and item not in common:
     common.append(item)
print(common)

# Question 13: Create a list of lists: [[1, 2], [3, 4], [5, 6]]
print("\nQuestion 13: Create a list of lists: [[1, 2], [3, 4], [5, 6]]")
# Your code here
list = [[1,2],[3,4],[5,6]]



# Question 14: Find the sum of each sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 14: Find the sum of each sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here
import math
list = [[1,2,3],[4,5,6],[7,8,9]]
sums = []
for item in list:
    total = 0
    for i in item:
        total+=i
    sums.append(total)
print(sums)

# Question 15: Transpose the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 15: Transpose the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here
matrix = [[1,2,3], [4,5,6], [7,8,9]]
transpose = []
for i in range(len(matrix[0])):
    new_row = []
    for j in range(len(matrix)):
        new_row.append(matrix[j][i])
    transpose.append(new_row)
for row in transpose:
    print(row)


# Question 16: Find the maximum value in each sublist of [[1, 5, 3], [9, 2, 7], [4, 8, 6]]
print("\nQuestion 16: Find the maximum value in each sublist of [[1, 5, 3], [9, 2, 7], [4, 8, 6]]")
# Your code here
matrix = [[1,5,3],[9,2,7],[4,8,6]]
max = []
for item in matrix:
    max_row = item[0]
    for i in item:
        if i>max_row:
            max_row = i
    max.append(max_row)
print(max)
        


# Question 17: Create a 3D list: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("\nQuestion 17: Create a 3D list: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")
# Your code here
three_d_list = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

print(three_d_list)

# Question 18: Find the sum of all elements in 3D list [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("\nQuestion 18: Find the sum of all elements in 3D list [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")
# Your code here
list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
sum = 0
for items in list:
    for item in items:
        for i in item:
            sum += i
print(sum)
 
# Question 19: Extract all even numbers from nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 19: Extract all even numbers from nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even = []
for items in list:
    for item in items:
            if item%2 == 0:
                even.append(item)
print(even)


# Question 20: Create a list of mixed data types: [1, "hello", 3.14, True, [1, 2, 3]]
print("\nQuestion 20: Create a list of mixed data types: [1, 'hello', 3.14, True, [1, 2, 3]]")
# Your code here
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
print(mixed_list)

# Question 21: Find the length of each string in ["apple", "banana", "cherry", "date"]
print("\nQuestion 21: Find the length of each string in ['apple', 'banana', 'cherry', 'date']")
# Your code here
list = ["apple", "banana", "cherry", "date"]
lengths = []
for items in list:
   x = len(items)
   lengths.append(x)
print(lengths)
# Question 22: Create a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')]
print("\nQuestion 22: Create a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')]")
# Your code here
tuple_list = [(1, 'a'), (2, 'b'), (3, 'c')]
print(tuple_list)

# Question 23: Extract first element from each tuple in [(1, 'a'), (2, 'b'), (3, 'c')]
print("\nQuestion 23: Extract first element from each tuple in [(1, 'a'), (2, 'b'), (3, 'c')]")
# Your code here
tuple_list = [(1, 'a'), (2, 'b'), (3, 'c')]
for i in tuple_list:
    print(i[0],end = ' ')

# Question 24: Create a list of dictionaries: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
print("\nQuestion 24: Create a list of dictionaries: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]")
# Your code here
people = [{'name': 'Alice', 'age': 25},{'name': 'Bob', 'age': 30}]
print(people)

# Question 25: Extract all 'name' values from list of dictionaries
print("\nQuestion 25: Extract all 'name' values from list of dictionaries")
# Your code here
print("\nQuestion 25: Extract all 'name' values from list of dictionaries")

people = [{'name': 'Alice', 'age': 25},{'name': 'Bob', 'age': 30}]
names = []
for person in people:
    names.append(person['name'])

print(names)

# Question 26: Find the person with maximum age in list of dictionaries
print("\nQuestion 26: Find the person with maximum age in list of dictionaries")
# Your code here
people = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
max_age = 0
oldest = ""
for person in people:
    if person['age'] > max_age:
        max_age = person['age']
        oldest = person['name']
print(oldest, "is the oldest with age", max_age)

# Question 27: Create a 4D list: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]
print("\nQuestion 27: Create a 4D list: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]")
# Your code here
four_d_list = [[[[1, 2], [3, 4]],[[5, 6], [7, 8]]],[[[9, 10], [11, 12]],[[13, 14], [15, 16]]]]
print(four_d_list)


# Question 28: Find the maximum value in 4D list
print("\nQuestion 28: Find the maximum value in 4D list")
# Your code here
matrix = [[[[1, 2], [3, 4]],[[5, 6], [7, 8]]],[[[9, 10], [11, 12]],[[13, 14], [15, 16]]]]
max = 0
for items in matrix:
    for item in items:
        for i in item:
            for x in i:
             if x > max:
                max = x
print(max)

# Question 29: Create a list of sets: [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
print("\nQuestion 29: Create a list of sets: [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]")
# Your code here
list_of_sets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
print(list_of_sets)
# Question 30: Find the union of all sets in list of sets
print("\nQuestion 30: Find the union of all sets in list of sets")
# Your code here
list_of_sets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
union_set = set.union(*list_of_sets)
print("Union of all sets:", union_set)


# Question 31: Create a list of complex numbers: [1+2j, 3+4j, 5+6j]
print("\nQuestion 31: Create a list of complex numbers: [1+2j, 3+4j, 5+6j]")
# Your code here
list = [1+2j, 3+4j, 5+6j]
print(list)

# Question 32: Find the magnitude of each complex number in list
print("\nQuestion 32: Find the magnitude of each complex number in list")
# Your code here
list = [1+2j, 3+4j, 5+6j]
magnitude = []
for num in list:
    magnitude.append(abs(num))
print(magnitude)
# Question 33: Create a nested list with different levels: [1, [2, 3], [4, [5, 6]], 7]
print("\nQuestion 33: Create a nested list with different levels: [1, [2, 3], [4, [5, 6]], 7]")
# Your code here
nested_list = [1, [2, 3], [4, [5, 6]], 7]
print(nested_list)
# Question 34: Count the depth of nesting in [1, [2, 3], [4, [5, 6]], 7]
print("\nQuestion 34: Count the depth of nesting in [1, [2, 3], [4, [5, 6]], 7]")
# Your code here

# Question 35: Create a list of functions: [len, str, int, float]
print("\nQuestion 35: Create a list of functions: [len, str, int, float]")
# Your code here
functions = [len, str, int, float]

print(functions)                
print(functions[0]("hello"))   
print(functions )    
print(functions[2]("456"))    
print(functions[3]("3.14"))   

# Question 36: Apply each function in list to string "123"
print("\nQuestion 36: Apply each function in list to string '123'")
# Your code here
functions = [len, str, int, float]
input_str = "123"

results = []

for func in functions:
    result = func(input_str)
    results.append(result)

print(results)

# Question 37: Create a list of lambda functions: [lambda x: x*2, lambda x: x**2, lambda x: x+1]
print("\nQuestion 37: Create a list of lambda functions: [lambda x: x*2, lambda x: x**2, lambda x: x+1]")
# Your code here
funcs = [lambda x: x*2, lambda x: x**2, lambda x: x+1]

# Question 38: Apply each lambda function to 5
print("\nQuestion 38: Apply each lambda function to 5")
# Your code here
funcs = [lambda x: x*2, lambda x: x**2, lambda x: x+1]
for f in funcs:
    print(f(5))
# Question 39: Create a list of classes: [list, dict, set, tuple]
print("\nQuestion 39: Create a list of classes: [list, dict, set, tuple]")
# Your code here
classes = [list, dict, set, tuple]
# Question 40: Create instances of each class in list
print("\nQuestion 40: Create instances of each class in list")
# Your code here
classes = [list, dict, set, tuple]
instances = [cls for cls in classes]

for instance in instances:
    print(instance)

# Question 41: Create a list of None values: [None, None, None, None]
print("\nQuestion 41: Create a list of None values: [None, None, None, None]")
# Your code here
list1 = ["None","None","None","None"]
print(list1)
# Question 42: Replace all None values with 0 in list
print("\nQuestion 42: Replace all None values with 0 in list")
# Your code here
list1 = [None, None, None, None]
for i in range(len(list1)):
    if list1[i] is None:
        list1[i] = 0
print(list1)
# Question 43: Create a list of boolean values: [True, False, True, False]
print("\nQuestion 43: Create a list of boolean values: [True, False, True, False]")
# Your code here
bool_list = [True, False, True, False]
print(bool_list)

# Question 44: Count True values in boolean list
print("\nQuestion 44: Count True values in boolean list")
# Your code here
bool_list = [True, False, True, False]
count = 0
for item in bool_list:
    if item == True:
        count += 1  
print(count)


# Question 45: Create a list of ranges: [range(3), range(5), range(2)]
print("\nQuestion 45: Create a list of ranges: [range(3), range(5), range(2)]")
# Your code here
ranges = [range(3), range(5), range(2)]
print(ranges)

# Question 46: Convert each range to list
# print("\nQuestion 46: Convert each range to list")
ranges = [range(3), range(5), range(2)]


# Question 47: Create a list of generators: [(x for x in range(3)), (x for x in range(5))]
print("\nQuestion 47: Create a list of generators: [(x for x in range(3)), (x for x in range(5))]")
# Your code here
generators = [(x for x in range(3)), (x for x in range(5))]
print(generators)

# Question 48: Convert each generator to list
print("\nQuestion 48: Convert each generator to list")
# Your code here
generators = [(x for x in range(3)), (x for x in range(5))]

for g in generators:
    result = []
    for item in g:
        result.append(item)
    print(result)

# Question 49: Create a list of iterators: [iter([1, 2, 3]), iter([4, 5, 6])]
print("\nQuestion 49: Create a list of iterators: [iter([1, 2, 3]), iter([4, 5, 6])]")
# Your code here
iterators = [iter([1, 2, 3]), iter([4, 5, 6])]
# Question 50: Extract all elements from each iterator
print("\nQuestion 50: Extract all elements from each iterator")
# Your code here 
for it in iterators:
    elements = []
    for item in it:
        elements.append(item)
    print(elements)