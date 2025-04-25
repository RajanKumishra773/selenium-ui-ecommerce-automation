a = 2
print(a << 1)

def my_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()