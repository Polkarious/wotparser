from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://ru.wargaming.net/shop/wot/main/"
driver = webdriver.Chrome()
driver.get(url)

soup = BeautifulSoup(driver.page_source, features="html.parser")

shop_items_list = []

for article in soup.find_all("article"):
    name = article.find("div", class_="item_footer").find("span", class_="item_name").text

    if name == "Любое количество золота":
        continue

    price_new = article.find("span", class_="js-price").text
    price_old = article.find("span", class_="price_old").find("span", class_="js-price")

    if price_old is None:
        price_old = "-"
    else:
        price_old = price_old.text

    shop_items_list.append({"name": name, "price new": price_new, "price old": price_old})

print(shop_items_list)
