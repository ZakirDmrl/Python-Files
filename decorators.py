def my_decorator(func):
    def wrapper():
        print("fornsiyondan önce işlemler")
        func()
        print("fonsiyondan sonrki işlemler")
    return wrapper

def sayHello():
    print("Hello")

def Gretting():
    print("gretting")

sayHello = my_decorator(sayHello)
sayHello()