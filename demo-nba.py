import pandas as pd

df = pd.read_csv("datasets/player_data.csv")

# # 1-İlk 10 kaydı getiriniz.
# result = df.head(10)
# print(result)

# #2-Toplam kaç kayıt vardır?
# result = len(df.index)
# print(result)

# #3-Oyuncuların dbaşlama tarihi ort ?
# result = df["year_start"].mean()
# print(result)

# #4-En geç başlayan ne zaman başladı?
# result = df["year_start"].max()
# print(result)

# #5-En geç başlayan kimdir?
# result = df[df["year_start"] == df["year_start"].max()]["name"]
# print(result)
# #6-end- yılı 1995-2010 yıl arasında olran oyuncuların isim ve doğum günlerini küçükten büyüyğe sıralı yazın
# result = df[(df["year_end"] >= 1995 ) & (df["year_end"] <= 2010)][["name","birth_date"]].sort_values("birth_date",ascending=False)
# print(result)

# #7-Alex Acker isimli oyuncunun okuduğu üniversite
result = df[df["name"] == "Alex Acker"]["college"].iloc[0]
print(result)

# #8-Toplam kaç college var
result = len(df.groupby("college")) #alternatif
result = df["college"].nunique() #alternatif
result = len(df["college"].unique()) #alternatif
print(result)
# #9-Her colege de kaç  oyuncu var
result = df["college"].value_counts()
print(result)
# #10-İsmi içinde Adams yazan kayıtları bul gerçek kayıtta değiştir
# df.dropna(inplace=True)
# result = df[df["name"].str.contains("Adams")] # gerçek kayıtta değişmez

print(result)