# Closure — Function বাইরের Variable মনে রাখে
def outer():

    name = "Imam"

    def inner():
        print(name)

    inner()


outer()