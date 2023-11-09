import torch
from sklearn.datasets import load_boston

x = torch.rand(10)

print(x)
print(x.size())

temp = torch.FloatTensor([12,21,42,4,12])

print(temp)
print(temp.size())

bostonHouses = load_boston()
print(bostonHouses)