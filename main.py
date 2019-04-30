from selenium import webdriver
from bs4 import BeautifulSoup

# url = "https://ru.wargaming.net/shop/wot/main/"
# driver = webdriver.Chrome()
# driver.get(url)
a = open("file.txt", "r", encoding="utf-8")
# soup = BeautifulSoup(driver.page_source, features="html.parser")
soup = BeautifulSoup(a, features="html.parser")
articles = soup.find_all("article")
lis = []
for article in articles:
    name = article.find("div", class_="item_footer").find("span", class_="item_name").text
    if name == "Любое количество золота":
        continue
    price_new = article.find("span", class_="js-price").text
    price_old = article.find("span", class_="price_old").find("span", class_="js-price")
    if price_old is None:
        price_old = "-"
    else:
        price_old = price_old.text
    dic = {"name": name, "price new": price_new, "price old": price_old}
    lis.append(dic)
print(lis)

