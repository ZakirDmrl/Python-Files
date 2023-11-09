from datetime import datetime
from datetime import timedelta
simdi = datetime.now() # = datetime.today
result = datetime.ctime(simdi)#Sun Mar  5 21:40:46 2023
result = datetime.strftime(simdi,'%Y') # year
result = datetime.strftime(simdi,'%X') #secend
result = datetime.strftime(simdi,'%d') # day int
result = datetime.strftime(simdi,'%A') # day str
result = datetime.strftime(simdi,'%B') # mount str

t = '5 Mart 2023'
gun,ay,yil = t.split()
print(gun)
print(ay)
print(yil)

t = "15 April 2019 hour 10:12:30"
dt = datetime.strptime(t,"%d %B %Y hour %H:%M:%S")
print(dt)
print(dt.year)
birthday = datetime(2004,10,9)
result = datetime.timestamp(birthday) # datetime change to secend
result = datetime.fromtimestamp(result) # second to datetime
result = datetime.fromtimestamp(0) # default date for PC
result = simdi - birthday # timedelta
result = result.days
print(simdi)
result = simdi + timedelta(days=10) # mevcut zamana 10 gün daha ekler
print(result) 

