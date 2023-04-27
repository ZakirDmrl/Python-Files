def square(num): return num ** 2

numbers = [1,2,3,4,5,9]

result = list(map(square, numbers))
print(result)
for item in map(square, numbers):
    print(item)
result = list(map(lambda num: num ** 2, numbers))
print(result)

check_even = lambda num: num%2==0
result  = list(filter(check_even,numbers))
print(result)