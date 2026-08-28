# Decorator — Function-এর Behavior পরিবর্তন/বাড়ানো

def decorator(func):
    def wrapper():
        print(" Transaction Start ")
        func()
        print(" Transaction End ")
    return wrapper

@decorator
def hello():
    print(" .... Executing all steps of  transaction .... ")

hello()