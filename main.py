from bs4 import BeautifulSoup
import requests
import csv

url = "https://health-diet.ru/base_of_food/food_24507/"
headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}

req = requests.get(url = url, headers = headers)

soup = BeautifulSoup(req.text, "html.parser")

table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
product = table_head[0].text
calories = table_head[1].text
belki = table_head[2].text
fats = table_head[3].text
uglevodi = table_head[4].text

with open("data.csv", "w", encoding='cp1251', newline='') as file:
    writer = csv.writer(file,  delimiter=";")
    writer.writerow(
        [product, calories, belki, fats, uglevodi]
    )

products_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")

for item in products_data:
    products_tds = item.find_all("td")

    title = products_tds[0].find("a").text
    cal = products_tds[1].text
    bel = products_tds[2].text
    fat = products_tds[3].text
    ugl = products_tds[4].text

    with open("data.csv", "a", encoding='cp1251', newline='') as file:
        writer = csv.writer(file,  delimiter=";")
        writer.writerow(
            [title, cal, bel, fat, ugl]
        )

url = "https://health-diet.ru/base_of_food/food_24501/"
headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}

req = requests.get(url=url, headers=headers)

soup = BeautifulSoup(req.text, "html.parser")

table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
product = table_head[0].text
cal = table_head[1].text
bel = table_head[2].text
fat = table_head[3].text
ugl = table_head[4].text

with open("data2.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow([product,cal, bel, fat, ugl])


table_info = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")

for item in table_info:
    products_tds = item.find_all("td")
    title = products_tds[0].find("a").text
    calories = products_tds[1].text
    belki = products_tds[2].text
    fats = products_tds[3].text
    uglevodi = products_tds[4].text

    with open("data2.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow([title, calories, belki, fats, uglevodi])
