import requests
from bs4 import BeautifulSoup


reponse = requests.get("https://books.toscrape.com").text
translate = BeautifulSoup(reponse,"html.parser")
print(translate.p)
