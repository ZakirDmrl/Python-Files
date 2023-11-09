import torch

rand1 = torch.rand(10000,10000)
rand2 = torch.rand(10000,10000)

print(rand1,rand2)
print(rand1+rand2)
print(torch.add(rand1,rand2))
print(rand1*rand2)
print(rand1.mul(rand2))