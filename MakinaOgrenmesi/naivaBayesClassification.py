import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv("MakinaOgrenmesi/urun.csv")

x = data.iloc[:,0:2].values
y = data["satinalma"].values.reshape(-1,1)

S = data[data["satinalma"] == 0]
M = data[data["satinalma"] == 1]

plt.scatter(S["yaş"],S["maaş"],color = "red")
plt.scatter(M["yaş"],M["maaş"],color = "blue")

# plt.show()


from sklearn.model_selection import train_test_split

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.33,random_state= 33)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

xtrain1 = sc.fit_transform(xtrain)
xtest1 = sc.transform(xtest)
 
# GaussianNB tahmin edeceğimiz veri ya da kolon sürekli 0.9090909090909091
# BernoulliNB tahmin edeceğimiz veri ya da kolon ikili ( aldı/almadı vs) 0.7045454545454546
# MultinomialNB tahmin edeceğimiz veri ya da kolon integer sayılardan oluşuyorsa
from sklearn.naive_bayes import GaussianNB

nb = GaussianNB()

nb.fit(xtrain1,ytrain)

yhead = nb.predict(xtest1)
print(nb.score(xtest1,ytest)) 

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(ytest,yhead)
print(cm)