from selenium import webdriver
from bs4 import BeautifulSoup

# url = "https://ru.wargaming.net/shop/wot/main/"
# driver = webdriver.Chrome()
# driver.get(url)
a = open("file.txt", "r", encoding="utf-8")
# soup = BeautifulSoup(driver.page_source, features="html.parser")
soup = BeautifulSoup(a, features="html.parser")
articles = soup.find_all("article")
for article in articles:
    name = article.find("div", class_="item_footer").find("span", class_="item_name").text
    if name == "Любое количество золота":
        continue
    price = article.find("span", class_="js-price").text
    price_2 = article.find("span", class_="price_old").text
    print(name, "-", "Со скидкой", price, ",", "Без скидки", price_2)
