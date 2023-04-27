import requests 
from bs4 import BeautifulSoup

url = "https://www.btkakademi.gov.tr/portal/course/player/deliver/sifirdan-ileri-seviye-python-programlama-5877"
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find.all()
print(list)