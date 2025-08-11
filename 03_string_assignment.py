# STRING DATATYPE ASSIGNMENT - 50 QUESTIONS
# ========================================

# SOLVED EXAMPLE
# --------------
# Question: Count vowels in the string "Hello World"
print("SOLVED EXAMPLE:")
print("Count vowels in the string 'Hello World'")
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"String: {text}")
print(f"Number of vowels: {count}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Reverse the string "Python Programming"
print("Question 1: Reverse the string 'Python Programming'")
# Your code here
string = 'Python Programming'
print(string[::-1])

# Question 2: Check if "racecar" is a palindrome
print("\nQuestion 2: Check if 'racecar' is a palindrome")
# Your code here
code = 'racecar'
code1 = code[::-1]
if code == code1:
    print("It is a palindrome")

# Question 3: Count the number of words in "Python is a great programming language"
print("\nQuestion 3: Count the number of words in 'Python is a great programming language'")
# Your code here
string ="Python is a great programming language"
print(len(string))

# Question 4: Convert "hello world" to title case
print("\nQuestion 4: Convert 'hello world' to title case")
# Your code here
string ='hello world' 
print(string.title())

# Question 5: Find the length of string "Data Science"
print("\nQuestion 5: Find the length of string 'Data Science'")
# Your code here
print(len('Data Science'))

# Question 6: Replace all spaces with underscores in "Machine Learning"
print("\nQuestion 6: Replace all spaces with underscores in 'Machine Learning'")
# Your code here
string ='Machine Learning'
x = string.replace(' ', '_')
print(x)

# Question 7: Check if "python" is in "Python Programming Language"
print("\nQuestion 7: Check if 'python' is in 'Python Programming Language'")
# Your code here
print('Python' in 'Python Programming Language')

# Question 8: Extract the first 5 characters from "Artificial Intelligence"
print("\nQuestion 8: Extract the first 5 characters from 'Artificial Intelligence'")
# Your code here
string = "Artificial Intelligence"
x=string[0:5]
print(x)

# Question 9: Convert "UPPERCASE" to lowercase
print("\nQuestion 9: Convert 'UPPERCASE' to lowercase")
# Your code here
stg = 'UPPERCASE'
print(stg.lower())

# Question 10: Remove all vowels from "Computer Science"
print("\nQuestion 10: Remove all vowels from 'Computer Science'")
# Your code here
vowels = ['a','e','i','o','u']
stg = "Computer Science"
for i in stg:
    if i not in vowels:
       print(i, end = '')


# Question 11: Find the most frequent character in "mississippi"
print("\nQuestion 11: Find the most frequent character in 'mississippi'")
# Your code here
stng = "mississippi"
max_count = 0
max_char = ' '
for i in stng:
    count = stng.count(i)
    if max_count < count:
        max_count = count
        max_char = i
print(max_char)
        


# Question 12: Check if two strings are anagrams: "listen" and "silent"
print("\nQuestion 12: Check if two strings are anagrams: 'listen' and 'silent'")
# Your code here
str1 ='listen'
str2 ='silent'
if sorted(str1) == sorted(str2):
    print('anagrams')


# Question 13: Capitalize first letter of each word in "python programming language"
print("\nQuestion 13: Capitalize first letter of each word in 'python programming language'")
# Your code here
str = "python programming language"
print(str.title())

# Question 14: Count consonants in "Hello World"
print("\nQuestion 14: Count consonants in 'Hello World'")
# Your code here
str = 'Hello World'
vowels = 'aeiou '
count = 0
for i in str:
    if i not in vowels:
        count += 1
print(count)

# Question 15: Find the longest word in "Python is a programming language"
print("\nQuestion 15: Find the longest word in 'Python is a programming language'")
# Your code here
str = "Python is a programming language"
x = str.split()
max_word = ' '
max_len = 0 
for i in x:
    if len(i) > max_len:
        max_len = len(i)
        max_word = i
print(max_word)


# Question 16: Remove all punctuation from "Hello, World! How are you?"
print("\nQuestion 16: Remove all punctuation from 'Hello, World! How are you?'")
# Your code here
import string
str = 'Hello, World! How are you?'
for char in str:
    if char not in string.punctuation:
        print(char, end = '')


# Question 17: Check if string starts with "Python"
print("\nQuestion 17: Check if string starts with 'Python'")
# Your code here
string = 'Python'
print(string.startswith('Python'))

# Question 18: Find the index of first occurrence of 'o' in "Hello World"
print("\nQuestion 18: Find the index of first occurrence of 'o' in 'Hello World'")
# Your code here
str ="Hello World"
print(str.index('o'))

# Question 19: Split string "apple,banana,orange" by comma
print("\nQuestion 19: Split string 'apple,banana,orange' by comma")
# Your code here
str = 'apple,banana,orange'
str1 = str.split(',')
print(str1[0])

# Question 20: Join list ['Python', 'is', 'awesome'] with spaces
print("\nQuestion 20: Join list ['Python', 'is', 'awesome'] with spaces")
# Your code here
list = ['Python','is','awesome']
list1 = ' '.join(list)
print(list1)

# Question 21: Check if string contains only digits: "12345"
print("\nQuestion 21: Check if string contains only digits: '12345'")
# Your code here
str = "12345" 
print(str.isalnum())

# Question 22: Check if string contains only letters: "HelloWorld"
print("\nQuestion 22: Check if string contains only letters: 'HelloWorld'")
# Your code here
str = "HelloWorld"
print(str.isalpha())

# Question 23: Convert "hello world" to "hElLo WoRlD" (alternating case)
print("\nQuestion 23: Convert 'hello world' to 'hElLo WoRlD' (alternating case)")
# Your code here
s = "hello world"
result = ""
for i, ch in enumerate(s):
    if i % 2 == 0:
        result += ch.lower()
    else:
        result += ch.upper()
print(result)

# Question 24: Find all positions of 'a' in "banana"
print("\nQuestion 24: Find all positions of 'a' in 'banana'")
# Your code here
str = "banana apple"
Positions = []
for i in range(0,len(str)):
    if str[i] == 'a':
        Positions.append(i)
print(Positions)

# Question 25: Remove leading and trailing whitespace from "  Hello World  "
print("\nQuestion 25: Remove leading and trailing whitespace from '  Hello World  '")
# Your code here
str = "  Hello World  "
print(str.strip())


# Question 26: Check if string ends with "ing": "programming"
print("\nQuestion 26: Check if string ends with 'ing': 'programming'")
# Your code here
str = 'programming'
print(str.endswith('ing'))

# Question 27: Replace first occurrence of 'o' with '0' in "Hello World"
print("\nQuestion 27: Replace first occurrence of 'o' with '0' in 'Hello World'")
# Your code here
str = "Hello World"
x = str.replace('o','0',1)
print(x)

# Question 28: Find the shortest word in "Python is a programming language"
print("\nQuestion 28: Find the shortest word in 'Python is a programming language'")
# Your code here
str = "Python is a programming language"
x = str.split()
length = len(str)
shortest_word = ' '
for item in x:
    if length > len(item):
        length = len(item)
        shortest_word = item
print(shortest_word)


# Question 29: Count words that start with 'p' in "Python programming is powerful"
print("\nQuestion 29: Count words that start with 'p' in 'Python programming is powerful'")
# Your code here
str = "Python programming is powerful"
x = str.split()
count = 0
for item in x:
    if item.startswith('p'):
        count += 1
print(count)

# Question 30: Reverse words in "Hello World Python"
print("\nQuestion 30: Reverse words in 'Hello World Python'")
# Your code here
str = "Hello World Python"
x = str.split()
x.reverse()
reversed = ' '.join(x)
print(reversed)

# Question 31: Check if string is a valid email format: "user@example.com"
print("\nQuestion 31: Check if string is a valid email format: 'user@example.com'")
# Your code here
email = "user@example.com"
if '@' in email and '.' in email and email.index('@') < email.index('.'):
    print("Valid email")
else:
    print("Invalid email")

# Question 32: Extract domain from "https://www.example.com/path"
print("\nQuestion 32: Extract domain from 'https://www.example.com/path'")
# Your code here
url= "https://www.example.com/path"
x = url.split('//')[-1].split('/')[0]
print(x)


# Question 33: Count lines in multi-line string
print("\nQuestion 33: Count lines in multi-line string")
# Your code here
text = """Hello
World
This is
a multi-line
string"""
x = text.splitlines()
print(len(x))

# Question 34: Find common characters between "hello" and "world"
print("\nQuestion 34: Find common characters between 'hello' and 'world'")
# Your code here
a = 'hello'
b = 'world'
common_char = set(a) & set(b) #intersection of unique elements in a and b
print(common_char)

# Question 35: Check if string is a valid phone number: "+1-555-123-4567"
print("\nQuestion 35: Check if string is a valid phone number: '+1-555-123-4567'")
# Your code here
s = "+1-555-123-4567"

parts = s.split("-")
if s.startswith("+") and len(parts) == 4 and parts[0] == "+1" and \
   parts[1].isdigit() and len(parts[1]) == 3 and \
   parts[2].isdigit() and len(parts[2]) == 3 and \
   parts[3].isdigit() and len(parts[3]) == 4:
    print("Valid phone number")
else:
    print("Invalid phone number")

# Question 36: Extract numbers from "abc123def456ghi789"
print("\nQuestion 36: Extract numbers from 'abc123def456ghi789'")
# Your code here
str = 'abc123def456ghi7890'
y = '1234567890'
for item in str:
  if item in y:
     print(item,end = '')

# Question 37: Convert "snake_case" to "camelCase"
print("\nQuestion 37: Convert 'snake_case' to 'camelCase'")
# Your code here
s = "snake_case"
parts = s.split("_")
camel = parts[0] + "".join(word.capitalize() for word in parts[1:])
print(camel)

# Question 38: Check if string is a valid palindrome ignoring case: "A man a plan a canal Panama"
print("\nQuestion 38: Check if string is a valid palindrome ignoring case: 'A man a plan a canal Panama'")
# Your code here
str = "A man a plan a canal Panama"
x = str.replace(' ','').lower()
if x == x[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
# Question 39: Find the most common word in "the quick brown fox jumps over the lazy dog"
print("\nQuestion 39: Find the most common word in 'the quick brown fox jumps over the lazy dog'")
# Your code here
text = "the quick brown fox jumps over the lazy dog"
words = text.split() 
word_count  = 0
word_text  = ' '
for word in words:
    count  = words.count(word)
    if count > word_count:
        word_count  = count
        word_text  = word
        print(word_text)


# Question 40: Generate acronym from "National Aeronautics and Space Administration"
print("\nQuestion 40: Generate acronym from 'National Aeronautics and Space Administration'")
# Your code here
text  = 'National Aeronautics and Space Administration'
words  = text.split()
for word in words:
    if word != 'and':
      acronym = ''.join(word[0])
      print(acronym, end='')

# Question 41: Check if string contains balanced parentheses: "((()))"
print("\nQuestion 41: Check if string contains balanced parentheses: '((()))'")
# Your code here
text = "((())))))"
if text.count('(') == text.count(')'):
       print('Balanced')
else:
       print('Not balanced')

# Question 42: Convert "hello world" to Morse code
print("\nQuestion 42: Convert 'hello world' to Morse code")
# Your code here
morse = {'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.',
         'g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..',
         'm':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.',
         's':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-',
         'y':'-.--','z':'--..',' ':'/'}

s = "hello world"
print(" ".join(morse[ch] for ch in s.lower()))

# Question 43: Find the longest common substring between "programming" and "grammar"
print("\nQuestion 43: Find the longest common substring between 'programming' and 'grammar'")
# Your code here
s1 = "programming"
s2 = "grammar"
longest = ""

for i in range(len(s1)):
    for j in range(i+1, len(s1)+1):
        sub = s1[i:j]
        if sub in s2 and len(sub) > len(longest):
            longest = sub

print(longest)

# Question 44: Check if string is a valid URL: "https://www.google.com"
print("\nQuestion 44: Check if string is a valid URL: 'https://www.google.com'")
# Your code here
s = "https://www.google.com"
if s.startswith("http://") or s.startswith("https://"):
    print("Valid URL")
else:
    print("Invalid URL")

# Question 45: Extract all words with length > 5 from "Python programming is amazing and powerful"
print("\nQuestion 45: Extract all words with length > 5 from 'Python programming is amazing and powerful'")
# Your code here
s = "Python programming is amazing and powerful"
words = s.split()
result = []
for word in words:
    if len(word) > 5:
        result.append(word)
print(result)

# Question 46: Convert "hello world" to Pig Latin
print("\nQuestion 46: Convert 'hello world' to Pig Latin")
# Your code here
s = "hello world"
words = s.split()
result = []

for word in words:
    pig_word = word[1:] + word[0] + "ay"
    result.append(pig_word)

print(" ".join(result))

# Question 47: Check if string is a valid IPv4 address: "192.168.1.1"
print("\nQuestion 47: Check if string is a valid IPv4 address: '192.168.1.1'")
# Your code here
s = "192.168.1.1"
parts = s.split(".")

if len(parts) == 4:
    valid = True
    for part in parts:
        if not part.isdigit() or int(part) < 0 or int(part) > 255:
            valid = False
            break
    if valid:
        print("Valid IPv4 address")
    else:
        print("Invalid IPv4 address")
else:
    print("Invalid IPv4 address")

# Question 48: Find all substrings of "abc"
print("\nQuestion 48: Find all substrings of 'abc'")
# Your code here
s = "abc"
result = []
for start in range(len(s)):
    for end in range(start + 1, len(s) + 1):
        result.append(s[start:end])
print(result)

# Question 49: Convert "hello world" to ROT13 encoding
print("\nQuestion 49: Convert 'hello world' to ROT13 encoding")
# Your code here
s = "hello world"
result = ""

for ch in s:
    if ch.isalpha():
        base = 'a' if ch.islower() else 'A'
        result += chr((ord(ch) - ord(base) + 13) % 26 + ord(base))
    else:
        result += ch

print(result)

# Question 50: Check if string is a valid credit card number: "4532015112830366"
print("\nQuestion 50: Check if string is a valid credit card number: '4532015112830366'")
# Your code here 
s = "4532015112830366"
total = 0
reverse = s[::-1]

for i in range(len(reverse)):
    digit = int(reverse[i])
    if i % 2 == 1:
        digit *= 2
        if digit > 9:
            digit -= 9
    total += digit

if total % 10 == 0 and s.isdigit():
    print("Valid credit card number")
else:
    print("Invalid credit card number")
