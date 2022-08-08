from bs4 import BeautifulSoup
import requests
import json
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


# без энкодинга ошибка
with open('index.html', encoding='utf-8-sig') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
all_products_href = soup.find_all(class_='mzr-tc-group-item-href')


all_categories_dct = {}
for item in all_products_href:
    item_text = item.text
    item_href = "http://health-diet.ru" + item.get('href')
    # print(f'{item_text}: {item_href}')

    # пополняем словарь
    all_categories_dct[item_text] = item_href


# сохраняем JSON file
with open('all_categories_dct.json', 'w', encoding='utf-8') as file:
    json.dump(all_categories_dct, file, indent=4, ensure_ascii=False)
