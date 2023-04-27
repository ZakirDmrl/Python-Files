def cube():
    
    for i in range(5):
        yield i ** 3

#Bellek kullanmadan yapıldığı için performans artar.
generator = cube()
iterator = iter(generator)
while True:
    try:
        print(next(iterator))

    except StopIteration:
        break
#OR

for i in cube():
    print(i)

#different way comprehensive(kapsayıcı)

generator = (i**3 for i in range(5))
for i in generator:
    print(i)