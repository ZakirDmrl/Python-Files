import pandas as pd
import numpy as np

numbers = [20,30,40,50]
letters = ['a','b','c','d']
scalar = 5
pandas_series = pd.Series(numbers)
pandas_series = pd.Series(letters)
pandas_series = pd.Series()
pandas_series = pd.Series(5,[0,1,2,3])
pandas_series = pd.Series(numbers,['a','b','c','d'])
dict = {'a':10,'b':20,'c':30,'d':40}
pandas_series = pd.Series(dict)
random_numbers = np.random.randint(10,100,6)
pandas_series = pd.Series(random_numbers)
pandas_series = pd.Series([20,30,40,50],['a','b','c','d'])
result = pandas_series['a']
print(result)

result = pandas_series[['a','c']]
print(result)


result = pandas_series[:2] #ilk 2 
print(result)
result = pandas_series[-2:] #son 2
print(result)
result = pandas_series.ndim # kaç boyutlu ?
print(result)
result = pandas_series.shape # kaç (satır,sütün) ?
print(result)
result = pandas_series.sum()
print(result)
result = pandas_series.max()
print(result)
result = pandas_series + pandas_series
print(result)
result = pandas_series * 50
print(result)
result = np.sqrt(pandas_series)
print(result)
result = pandas_series >= 50
print(result)
result = pandas_series % 2 == 0
print(pandas_series[result])
print(pandas_series % 2 == 0)
print(pandas_series)

print(result)


opel2018 =pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 =pd.Series([60,30,20,10],["astra","corsa","mokka","grandland"])
total = opel2018 + opel2019
print(total["astra"])
