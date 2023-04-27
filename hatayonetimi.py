def factorial(number):
    if not isinstance(number,int):
        raise TypeError("Number must be an integer")
    if number < 0:
        raise ValueError("Number couldn't negative.")
    def inner_factorial(number):
        if number <= 1:
            return 1
        
        return number * inner_factorial(number-1)
    return inner_factorial(number)

result = factorial(-1)
print(result)