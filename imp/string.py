# ============================================================
#           PYTHON STRING — ONLY IMPORTANT
# ============================================================


# 1️⃣ STRING CREATE
name = "Imam"
language = 'Python'

print(name)
print(language)


# 2️⃣ LENGTH — len()
text = "Python"

print(len(text))        # 6


# 3️⃣ INDEXING
text = "Python"

print(text[0])          # P
print(text[1])          # y
print(text[-1])         # n


# 4️⃣ SLICING ⭐⭐⭐
text = "Python Programming"

print(text[0:6])        # Python
print(text[7:])         # Programming
print(text[:6])         # Python
print(text[::2])        # Every 2nd character
print(text[::-1])       # Reverse


# 5️⃣ CONCATENATION — +
first = "Imam"
last = "Hossain"

full_name = first + " " + last

print(full_name)


# 6️⃣ f-STRING ⭐⭐⭐
name = "Imam"
age = 22

print(f"My name is {name} and I am {age} years old.")


# 7️⃣ lower() / upper()
text = "PyThOn"

print(text.lower())     # python
print(text.upper())     # PYTHON


# 8️⃣ strip() ⭐⭐⭐
text = "   Python   "

print(text.strip())     # Python


# 9️⃣ replace() ⭐⭐⭐
text = "I love JavaScript"

text = text.replace("JavaScript", "Python")

print(text)


# 🔟 split() ⭐⭐⭐
text = "Python is easy"

words = text.split()

print(words)
# ['Python', 'is', 'easy']


# 1️⃣1️⃣ join() ⭐⭐⭐
words = ["Python", "is", "easy"]

text = " ".join(words)

print(text)
# Python is easy


# 1️⃣2️⃣ find()
text = "I love Python"

print(text.find("Python"))   # position


# 1️⃣3️⃣ count()
text = "banana"

print(text.count("a"))       # 3


# 1️⃣4️⃣ in / not in ⭐⭐⭐
text = "I am learning Python"

print("Python" in text)      # True
print("Java" in text)        # False


# 1️⃣5️⃣ startswith() / endswith()
file = "profile.jpg"

print(file.startswith("profile"))
print(file.endswith(".jpg"))


# 1️⃣6️⃣ STRING COMPARISON
a = "apple"
b = "banana"

print(a == b)
print(a != b)


# 1️⃣7️⃣ STRING + NUMBER
age = 22

# print("Age: " + age)       # ❌ Error

print("Age: " + str(age))    # ✅

# অথবা
print(f"Age: {age}")         # ⭐ Best


# 1️⃣8️⃣ USER INPUT ⭐⭐⭐
name = input("Enter your name: ")

print(f"Hello, {name}")


# 1️⃣9️⃣ CHECK STRING TYPE ⭐⭐
text = "Python"

print(text.isalpha())        # শুধু alphabet
print(text.isdigit())        # শুধু number
print(text.isalnum())        # alphabet + number


# 2️⃣0️⃣ PRACTICAL EXAMPLE ⭐⭐⭐

name = input("Enter your full name: ")

name = name.strip()
name = name.title()

print(f"Hello, {name}!")


# ============================================================
# ⭐ MOST IMPORTANT TO REMEMBER
# ============================================================

# len()
# indexing
# slicing
# +
# f-string
# lower()
# upper()
# strip()
# replace()
# split()
# join()
# find()
# count()
# in / not in
# startswith()
# endswith()
# input()
# str()
# ============================================================