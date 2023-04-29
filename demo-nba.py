import pandas as pd

df = pd.read_csv("datasets/player_data.cvs")

# 1-İlk 10 kaydı getiriniz.
result = df.head(n = 10)
print(result)