import requests
from bs4 import BeautifulSoup
manzil = "https://kun.uz/ru/news/2022/03/03/uzauto-motors-podnyala-tseny-na-avtomobili"
r = requests.get(manzil)
soup = BeautifulSoup(r.text,'html.parser')
javob = soup.find_all(class_='news-title')
print(javob[1].text)