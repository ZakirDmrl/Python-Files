import matplotlib.pyplot as plt
'''
# Stack Plot 
yil = [2011,2012,2013,2014,2015]

oyuncu1 = [8,10,12,7,9]
oyuncu2 = [7,12,5,15,21]
oyuncu3 = [18,20,21,25,19]


plt.plot ([],[],color="y",label="oyuncu1")
plt.plot ([],[],color="r",label="oyuncu2")
plt.plot ([],[],color="b",label="oyuncu3")


plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=['y','r','b'])
plt.title("Yıllara göre atılan goller")
plt.xlabel("yil")
plt.xlabel("gol sayisi")

plt.legend()
plt.show()
'''

'''
#Pasta dilimi Grafiği (Pie Graphs)
goal_types = 'Penaltı','Kaleye Atılan Şut','Serbest Vuruş'

goals = [12,35,7]
colors = ['y','r','b']

plt.pie(goals,labels=goal_types,colors=colors, shadow=True,explode=(0.05,0.05,0.05),autopct="%1.1f%%") # explode dilimler arası mesafe , autooct yüzdelik verme
plt.show()
'''
'''
#Bar Graph
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=0.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi",width=0.5)
plt.legend()
plt.xlabel("Gün")
plt.ylabel("Mesafe (km)")
plt.title("Araç Bilgileri")
plt.show()
'''

yaslar = [22,55,63,34,23,36,23,64,46,78,34,65,21,34,56,34,36,54,24,76,23,47,76,34,86,23,68,42,35,96,79,102,1,5,3,6,12,15]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)
plt.xlabel("Kişi Sayısı")
plt.ylabel("Yaş Grupları")
plt.title("Histogram Grafiği")
plt.show()