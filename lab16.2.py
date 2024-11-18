import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = input("Введіть URL веб-сторінки: ")

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

headings = {"H1": 0, "H2": 0, "H3": 0, "H4": 0, "H5": 0, "H6": 0}
for tag in headings.keys():
    headings[tag] = len(soup.find_all(tag.lower()))

plt.figure(figsize=(8, 6))
plt.bar(headings.keys(), headings.values(), color='skyblue', edgecolor='black')
plt.title("Частота використання заголовків H1-H6", fontsize=14)
plt.xlabel("Тип заголовка", fontsize=12)
plt.ylabel("Частота", fontsize=12)
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.show()
