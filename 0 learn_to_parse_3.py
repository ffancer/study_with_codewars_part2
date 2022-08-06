from bs4 import BeautifulSoup
import requests

# url = 'http://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
#
# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
#
# # сохранили инфу себе на комп, что б не забанили, кодировка что б небыло "?????"
# with open('index.html', 'w', encoding='utf-8-sig') as file:
#     file.write(src)


with open('index.html', encoding='utf-8-sig') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
all_products_href = soup.find_all(class_='mzr-tc-group-item-href')

for item in all_products_href:
    print(item)
