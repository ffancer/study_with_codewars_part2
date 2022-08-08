from bs4 import BeautifulSoup
import requests
import json
import csv
# url = 'http://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
#
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
#
# req = requests.get(url, headers=headers)
# src = req.text
#
# # сохранили инфу себе на комп, что б не забанили, кодировка что б небыло "?????"
# with open('index.html', 'w', encoding='utf-8-sig') as file:
#     file.write(src)


# без энкодинга ошибка
# with open('index.html', encoding='utf-8-sig') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
# all_products_href = soup.find_all(class_='mzr-tc-group-item-href')
#
#
# all_categories_dct = {}
# for item in all_products_href:
#     item_text = item.text
#     item_href = "http://health-diet.ru" + item.get('href')
#     # print(f'{item_text}: {item_href}')
#
#     # пополняем словарь
#     all_categories_dct[item_text] = item_href
#
#
# # сохраняем JSON file
# with open('all_categories_dct.json', 'w', encoding='utf-8') as file:
#     # indent = отступы, без нее все данные будут в строку; ensure помогает в работе с кириллицей и не экранирует
#     json.dump(all_categories_dct, file, indent=4, ensure_ascii=False)



with open('all_categories_dct.json', encoding='utf-8') as file:
    all_categories = json.load(file)
# print(all_categories)  # проверяем файл


# это делается что бы не бомбить запросами сайт
cnt = 0
for category_name, category_href in all_categories.items():
    if cnt == 0:
        lst = [',', '-', ' ', "'"]
        for item in lst:
            if item in category_name:
                category_name = category_name.replace(item, '_')
        req = requests.get(url=category_href, headers=headers)
        src = req.text

        with open(f'data/{cnt}_{category_name}.html', 'w', encoding='utf-8') as file:
            file.write(src)
        with open(f'data/{cnt}_{category_name}.html', encoding='utf-8') as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        # собираем загаловки таблицы
        table_head = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')
        # print(table_head)  тут метод .text не сработает но сработает ниже
        product = table_head[0].text
        calories = table_head[1].text
        proteins = table_head[2].text
        fats = table_head[3].text
        carbohydrates = table_head[4].text
        # , encoding='utf-8' в видео, но у меня и без него ок
        with open(f'data/{cnt}_{category_name}.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    product,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )

        cnt += 1
