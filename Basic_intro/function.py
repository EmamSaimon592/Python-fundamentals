# def function_Name():
#      code ....
# function_Name()



def add(a, b):
    return a + b

print(add(5, 3))


def student_info():
    print("Name: Imam")
    print("Department: CSE")
    print("University: IIUC")

student_info()



def greet(name):
    print("Hello", name , " I love u so Much")

greet("Faria")


def student(name, age, department):
    print("Name:", name)
    print("Age:", age)
    print("Department:", department)

student("Imam", 22, "CSE")



def multiple(a, b):
    return a * b

result = multiple(10, 10)
print(result)


# Function একাধিক value return করতে পারে
def calculate(a, b):
    return a + b, a - b, a * b
result = calculate(10, 5)
print(result)


# Nested Function

def outer_Function():
    
    def inner_function():
        print("Inner function")
    inner_function()

outer_Function()


# Lambda Function ছোট function এক লাইনে লেখার জন্য lambda ব্যবহার করা হয়।
square = lambda x: x * x
print(square(5)) 

# Lambda Multiple Arguments
add = lambda a, b: a + b
print(add(10, 20))
