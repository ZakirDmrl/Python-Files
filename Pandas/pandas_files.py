import pandas as pd
import sqlite3
df = pd.read_csv("player_data.csv")
print(df)
df = pd.read_json("intents.json")
print(df)
# df = pd.read_excel("player_data.xlsx")
connection = sqlite3.connect("sample.db")
df = pd.read_sql_query("SELECT * FROM students",connection)
print(df)
