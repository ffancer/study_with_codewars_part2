import random
from time import sleep

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
iteration_cnt = int(len(all_categories)) - 1
cnt = 0
print(f'Всего итерация {iteration_cnt}')
for category_name, category_href in all_categories.items():

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

    # проверка таблицы на наличие таблицы с продуктами
    alert_block = soup.find(class_='uk-alert-danger')
    if alert_block is not None:
        continue

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
        # сделав кортеж мы обошли то, что можно засунуть только один файл
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )
    # собираем данные продуктов
    products_data = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')
    product_info = []
    for item in products_data:
        product_tds = item.find_all('td')
        title = product_tds[0].find('a').text
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text
        product_info.append(
            {
                "Title": title,
                "Calories": calories,
                "Proteins": proteins,
                "Fats": fats,
                "Carbohydrates": carbohydrates
            }
        )
        with open(f'data/{cnt}_{category_name}.csv', 'a') as file:
            writer = csv.writer(file)
            # сделав кортеж мы обошли то, что можно засунуть только один файл
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )

    with open(f'data/{cnt}_{category_name}.json', 'a') as file:
        json.dump(product_info, file, indent=4, ensure_ascii=False)
    cnt += 1
    print(f'Итерация {cnt}, {category_name} записан...')
    iteration_cnt -= 1
    if iteration_cnt == 0:
        print('Работа завершена')
        break
    print(f'Осталось итерация {iteration_cnt}')
    sleep(random.randrange(2, 4))
