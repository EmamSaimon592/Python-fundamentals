# ============================================================
#              PYTHON STRING — A TO Z
# ============================================================


# ============================================================
# A — STRING কী?
# ============================================================

name = "Imam"
message = 'Hello Python'

print(name)
print(message)


# ============================================================
# B — STRING বানানোর বিভিন্ন উপায়
# ============================================================

single = 'Hello'
double = "Hello"

# Multiline String
text = """
This is
a multiline
string.
"""

print(single)
print(double)
print(text)


# ============================================================
# C — STRING CONCatenation
# String + String
# ============================================================

first_name = "Imam"
last_name = "Hossain"

full_name = first_name + " " + last_name

print(full_name)


# ============================================================
# D — STRING Data Type
# ============================================================

x = "Python"

print(type(x))


# ============================================================
# E — Escape Characters
# ============================================================

print("Hello\nWorld")      # New Line
print("Hello\tWorld")      # Tab
print("He said \"Hello\"") # Double quote
print('It\'s Python')     # Single quote
print("C:\\Users\\Imam")   # Backslash


# ============================================================
# F — f-string
# ============================================================

name = "Imam"
age = 22

print(f"My name is {name} and I am {age} years old.")


# ============================================================
# G — String Indexing
# ============================================================

word = "Python"

print(word[0])     # P
print(word[1])     # y
print(word[2])     # t
print(word[-1])    # n
print(word[-2])    # o


# ============================================================
# H — String Length
# len()
# ============================================================

word = "Python"

print(len(word))


# ============================================================
# I — String Immutability
# ============================================================

word = "Python"

# word[0] = "J"   # ERROR হবে

# String সরাসরি পরিবর্তন করা যায় না।
# নতুন String তৈরি করতে হয়।

word = "J" + word[1:]

print(word)


# ============================================================
# J — String Join
# ============================================================

words = ["Python", "is", "awesome"]

sentence = " ".join(words)

print(sentence)


# ============================================================
# K — String split()
# ============================================================

sentence = "Python is very easy"

result = sentence.split()

print(result)


# ============================================================
# L — lower()
# ============================================================

text = "PYTHON"

print(text.lower())


# ============================================================
# M — upper()
# ============================================================

text = "python"

print(text.upper())


# ============================================================
# N — capitalize()
# ============================================================

text = "python programming"

print(text.capitalize())


# ============================================================
# O — title()
# ============================================================

text = "python programming language"

print(text.title())


# ============================================================
# P — strip()
# Extra space remove করে
# ============================================================

text = "   Python   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())


# ============================================================
# Q — replace()
# ============================================================

text = "I love JavaScript"

new_text = text.replace("JavaScript", "Python")

print(new_text)


# ============================================================
# R — find()
# ============================================================

text = "I love Python"

print(text.find("Python"))
print(text.find("Java"))   # না পেলে -1


# ============================================================
# S — startswith() / endswith()
# ============================================================

text = "python.py"

print(text.startswith("python"))
print(text.endswith(".py"))


# ============================================================
# T — String Slicing
# ============================================================

text = "Python"

print(text[0:3])   # Pyt
print(text[2:])    # thon
print(text[:4])    # Pyth
print(text[:])     # Python

# Step
print(text[::2])
print(text[::-1])  # Reverse


# ============================================================
# U — in / not in
# ============================================================

text = "I am learning Python"

print("Python" in text)
print("Java" in text)

print("Java" not in text)


# ============================================================
# V — count()
# ============================================================

text = "banana"

print(text.count("a"))
print(text.count("na"))


# ============================================================
# W — String Validation Methods
# ============================================================

print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())

print("hello".islower())
print("HELLO".isupper())

print("Hello World".istitle())
print("   ".isspace())


# ============================================================
# X — String Formatting
# ============================================================

name = "Imam"
age = 22

# f-string
print(f"Name: {name}, Age: {age}")

# format()
print("Name: {}, Age: {}".format(name, age))

# Index দিয়ে
print("Name: {0}, Age: {1}".format(name, age))


# ============================================================
# Y — String Comparison
# ============================================================

a = "apple"
b = "banana"

print(a == b)
print(a != b)
print(a < b)
print(a > b)


# ============================================================
# Z — IMPORTANT STRING METHODS
# ============================================================

text = "python programming"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())

print(text.replace("python", "JavaScript"))
print(text.find("programming"))
print(text.count("m"))

print(text.startswith("python"))
print(text.endswith("ing"))

print("python" in text)

print(text.split())
print("-".join(["Python", "JavaScript", "C++"]))


# ============================================================
# BONUS — PRACTICAL STRING PROGRAM
# ============================================================

name = input("Enter your name: ")

# User input clean করা
name = name.strip()

# প্রথম অক্ষর Capital
name = name.title()

print(f"Hello, {name}!")


# ============================================================
# BONUS 2 — Username Generator
# ============================================================

first_name = input("First name: ").strip().lower()
last_name = input("Last name: ").strip().lower()

username = first_name + "_" + last_name

print("Your username:", username)


# ============================================================
# BONUS 3 — Password Checker
# ============================================================

password = input("Enter password: ")

if len(password) >= 8:
    print("Password length is OK")
else:
    print("Password must contain at least 8 characters")


# ============================================================
# BONUS 4 — Reverse String
# ============================================================

text = input("Enter a word: ")

reverse = text[::-1]

print("Reverse:", reverse)


# ============================================================
# BONUS 5 — Palindrome Checker
# ============================================================

text = input("Enter a word: ").lower()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# ============================================================
# END
# ============================================================