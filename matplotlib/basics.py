import matplotlib.pyplot as plt
import math
import numpy as np
'''
x = [-4,-3,-2,-1,0,1,2,3,4]
y = [16,9,4,1,0,1,4,9,16]
plt.plot(x,y,color="red") # fmt = [marker][line][color]
plt.axis([-6,6,0,20]) # x değerleri x eks. -6 dan 6 ya kadar y değerleri y eks. 0 dan 20 ye kadar.
plt.plot(x,y,"-g") 
plt.plot(x,y,"--g") # ilk parametere(-) çizginin style i 2. si ise(-g) ise rengi
plt.plot(x,y,"o:r")
plt.title("Grafik Başlığı")
plt.xlabel("x label")
plt.ylabel("y label")
plt.show()
'''

'''
x = np.linspace(0,2,100)
plt.plot(x , x ,label="linear")
plt.plot(x, x**2,label="quadratic")
plt.plot(x, x**3, label="cubic")
plt.title("Simple Plot")
plt.xlabel("x label")
plt.ylabel("y label")
plt.legend() # grafik adları yazar
plt.show()

'''

'''
x = np.linspace(0,2,100)
fig,axs= plt.subplots(3) # grafik sayısı
axs[0].plot(x,x,color="red")
axs[0].set_title("label1")
axs[1].plot(x,x**2,color="green")
axs[1].set_title("label2")
axs[2].plot(x,x**3,color="blue")
axs[2].set_title("label3")
plt.tight_layout() # yazılar alt alta gelmesi diye
plt.show()

'''
'''
x = np.linspace(0,2,100)
fig,axs= plt.subplots(2,2) # grafik sayısı 2 row 2 colomn
fig.suptitle("grafik başlığı")
axs[0,0].plot(x,x,color="red")
axs[0,1].plot(x,x**2,color="blue")
axs[1,0].plot(x,x**(-1),color="yellow")
axs[1,1].plot(x,x**(1/2),color="green")
plt.show()
'''
import pandas as pd
df = pd.read_csv("datasets/player_data.csv")
df = df.drop(["Number"],axis = 1).groupby("college").mean()
df.plot(subplots=True)
plt.legend()

plt.show()