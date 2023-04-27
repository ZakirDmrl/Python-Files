import random

result = random.random() # 0.0 - 1.0
result = random.random() * 100 # 0.0 - 100.0
result = int(random.uniform(1,10)) # 1-10
result = random.randint(1,20) # 1-20
names = ['ali','yağmur','deniz','cenk']
greeting = 'hello there'
result = names[random.randint(0,len(names)-1)] # listenin  kaç elemanlı olduğunu bilmediğimiz durumda
result = random.choice(names)
result = random.choice(greeting)
liste = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(liste) # 9, 4, 3, 7, 6, 1, 8, 0, 5, 2]
liste = range(100)
result = random.sample(liste,3) # listeden rastgele 3 eleman [94, 51, 34]
result = random.sample(names,2) #['ali', 'deniz']
print(result) 